import src.constants as constants

times = 0


def update(mobject):
    global times
    times += 1
    changed = []
    if times > 10:
        for i, dot in enumerate(mobject):
            if i in changed:
                continue
            times = 0
            if dot.color == constants.dark_blue:
                mobject[i].set_fill(constants.light_blue)

                if (1 + i) < len(mobject):
                    mobject[i + 1].set_fill(constants.dark_blue)
                else:
                    mobject[0].set_fill(constants.dark_blue)
                changed.append(i + 1)
