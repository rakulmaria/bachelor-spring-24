import os
import subprocess
import pytest

# Directory paths
test_directory = "./test/"
image_directory = "./media/images/"
test_image_directory = "./test/test_images/"
difference_image_directory = "test/image_difference/"

# Manim command template
manim_command_template = "manim -s {} {}"

# Image comparison command template
compare_command_template = "compare -metric AE {} {} {}"


def run_manim(file_path):
    # Extracting filename without extension
    filename = os.path.splitext(os.path.basename(file_path))[0]
    capitalized_filename = filename[0].upper() + filename[1:]

    # Running manim command
    manim_command = manim_command_template.format(file_path, filename)
    subprocess.run(manim_command, shell=True)

    # Running image comparison command
    image_path_manim = os.path.join(
        image_directory, filename, f"{capitalized_filename}_ManimCE_v0.18.0.png"
    )
    image_path_test = os.path.join(
        test_image_directory, f"{capitalized_filename}_ManimCE_v0.18.0.png"
    )
    difference_image_path = os.path.join(
        difference_image_directory, f"difference_{filename}.png"
    )

    compare_command = compare_command_template.format(
        image_path_manim, image_path_test, difference_image_path
    )
    result = subprocess.run(
        compare_command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    print("------------------")
    print(result.stderr)
    print("------------------")
    return result.stderr


@pytest.mark.parametrize(
    "filename",
    [f for f in os.listdir(test_directory) if f.endswith(".py") and f != "__init__.py"],
)
def test_images(filename):
    file_path = os.path.join(test_directory, filename)
    print(file_path)
    res = run_manim(file_path)
    assert res == "0"
