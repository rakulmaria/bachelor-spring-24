import src.colors as colors

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
            if dot.color == colors.dark_blue:
                mobject[i].set_fill(colors.light_blue)

                if (1 + i) < len(mobject):
                    mobject[i + 1].set_fill(colors.dark_blue)
                else:
                    mobject[0].set_fill(colors.dark_blue)
                changed.append(i + 1)
