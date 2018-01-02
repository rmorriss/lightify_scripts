from lightify import Lightify
import time
import random
import argparse
import sys

parser = argparse.ArgumentParser('Group Lighting Control')
parser.add_argument("-g", "--group", action='store', help="Enter the name of the group")
parser.add_argument("-l", "--light", action='store', help="Enter the name of a light in the group")
parser.add_argument("-a", "--action", nargs=1, help="Valid Actions are on, off, dim, bright, color, temp_up, temp_down, temp_min, temp_max")

if not sys.argv[1:]:
    sys.argv.extend(['-h'])

args = parser.parse_args(sys.argv[1:])

# the group should contain at least two lights

GATEWAY_ADDR = "192.168.1.13"
#LIGHT1 = 'Great Room 01'
LIGHT1 = args.light
#GROUP_NAME = 'Great Room'
GROUP_NAME = args.group
TIME = 0
print(args)

gateway = Lightify(GATEWAY_ADDR)
gateway.update_all_light_status()
gateway.update_group_list()

if args.group is not None:
    group = gateway.groups()[GROUP_NAME]
    lights = ([gateway.lights()[addr] for addr in group.lights()])

light = gateway.light_byname(LIGHT1)


class groups():

    def red():
        group.set_rgb(255, 0, 0, TIME)
        groups.COLOR_CHOICE = 'Red'

    def lime():
        group.set_rgb(0, 255, 0, TIME)
        groups.COLOR_CHOICE = 'Lime'

    def blue():
        group.set_rgb(0, 0, 255, TIME)
        groups.COLOR_CHOICE = 'Blue'

    def yellow():
        group.set_rgb(255, 255, 0, TIME)
        groups.COLOR_CHOICE = 'Yellow'

    def aqua():
        group.set_rgb(0, 255, 255, TIME)
        groups.COLOR_CHOICE = 'Agua'

    def magenta():
        group.set_rgb(255, 0, 255, TIME)
        groups.COLOR_CHOICE = 'Magenta'

    def silver():
        group.set_rgb(192, 192, 192, TIME)
        groups.COLOR_CHOICE = 'Silver'

    def gray():
        group.set_rgb(128, 128, 128, TIME)
        groups.COLOR_CHOICE = 'Gray'

    def maroon():
        group.set_rgb(128, 0, 0, TIME)
        groups.COLOR_CHOICE = 'Maroon'

    def olive():
        group.set_rgb(128, 128, 0, TIME)
        groups.COLOR_CHOICE = 'Olive'

    def green():
        group.set_rgb(0, 128, 0, TIME)
        groups.COLOR_CHOICE = 'Green'

    def purple():
        group.set_rgb(128, 0, 128, TIME)
        groups.COLOR_CHOICE = 'Purple'

    def teal():
        group.set_rgb(0, 128, 128, TIME)
        groups.COLOR_CHOICE = 'Teal'

    def navy():
        group.set_rgb(0, 0, 128 , TIME)
        groups.COLOR_CHOICE = 'Navy'

    def temp_up():
        old_on, old_lum, old_temp, old_r, old_g, old_b = gateway.update_light_status(light)
        global groups_temp
        if old_temp < 5801:
            for i in range(old_temp, old_temp + 500, 100):
                group.set_temperature(i, 0)
            groups_temp = i
        else:
            groups_temp = old_temp
            print("Already at Max")

    def temp_down():
        old_on, old_lum, old_temp, old_r, old_g, old_b = gateway.update_light_status(light)
        global groups_temp
        if old_temp > 2700:
            for i in range(old_temp, old_temp - 500, -100):
                group.set_temperature(i, 0)
            groups_temp = i
        else:
            groups_temp = old_temp
            print("Already at Min")

    def temp_max():
        group.set_temperature(6500, 0)
        global groups_temp
        groups_temp = 6500

    def temp_min():
        group.set_temperature(2200, 0)
        global groups_temp
        groups_temp = 2200

    def dim():
        old_on, old_lum, old_temp, old_r, old_g, old_b = gateway.update_light_status(light)
        global groups_level
        if old_lum > 20:
            for i in range(old_lum, old_lum - 20, -5):
                group.set_luminance(i, 0)
            groups_level = i
            time.sleep(0.5)
        else:
            groups_level = old_lum
            print("Already at Min")

    def bright():
        old_on, old_lum, old_temp, old_r, old_g, old_b = gateway.update_light_status(light)
        global groups_level
        if old_lum < 100:
            for i in range(old_lum, old_lum + 20, 5):
                group.set_luminance(i, 0)
            groups_level = i
            time.sleep(0.5)

        else:
            groups_level = old_lum
            print("Already at Max")

    def on():
        group.set_temperature(2500, 0)
        group.set_luminance(100, 0)
        group.set_onoff(1)

    def off():
        group.set_onoff(0)

    def color():
        random.choice(GROUP_COLORS)()

GROUP_COLORS = [groups.red, groups.lime, groups.blue, groups.yellow, groups.aqua, groups.magenta, groups.silver,
                    groups.gray, groups.maroon, groups.olive, groups.green, groups.purple, groups.teal, groups.navy]

class single():

    def red():
        light.set_rgb(255, 0, 0, TIME)
        single.COLOR_CHOICE = 'Red'

    def lime():
        light.set_rgb(0, 255, 0, TIME)
        single.COLOR_CHOICE = 'Lime'

    def blue():
        light.set_rgb(0, 0, 255, TIME)
        single.COLOR_CHOICE = 'Blue'

    def yellow():
        light.set_rgb(255, 255, 0, TIME)
        single.COLOR_CHOICE = 'Yellow'

    def aqua():
        light.set_rgb(0, 255, 255, TIME)
        single.COLOR_CHOICE = 'Aqua'

    def magenta():
        light.set_rgb(255, 0, 255, TIME)
        single.COLOR_CHOICE = 'Magenta'

    def silver():
        light.set_rgb(192, 192, 192, TIME)
        single.COLOR_CHOICE = 'Silver'

    def gray():
        light.set_rgb(128, 128, 128, TIME)
        single.COLOR_CHOICE = 'Gray'

    def maroon():
        light.set_rgb(128, 0, 0, TIME)
        single.COLOR_CHOICE = 'Maroon'

    def olive():
        light.set_rgb(128, 128, 0, TIME)
        single.COLOR_CHOICE = 'Olive'

    def green():
        light.set_rgb(0, 128, 0, TIME)
        single.COLOR_CHOICE = 'Green'

    def purple():
        light.set_rgb(128, 0, 128, TIME)
        single.COLOR_CHOICE = 'Purple'

    def teal():
        light.set_rgb(0, 128, 128, TIME)
        single.COLOR_CHOICE = 'Teal'

    def navy():
        light.set_rgb(0, 0, 128 , TIME)
        single.COLOR_CHOICE = 'Navy'

    def temp_up():
        old_on, old_lum, old_temp, old_r, old_g, old_b = gateway.update_light_status(light)
        global single_temp
        if old_temp < 5801:
            for i in range(old_temp, old_temp + 500, 100):
                light.set_temperature(i, 0)
                single_temp = i
        else:
            single_temp = old_temp
            print("Already at Max")

    def temp_down():
        old_on, old_lum, old_temp, old_r, old_g, old_b = gateway.update_light_status(light)
        global single_temp
        if old_temp > 2700:
            for i in range(old_temp, old_temp - 500, -100):
                light.set_temperature(i, 0)
                single_temp = i
        else:
            single_temp = old_temp
            print("Already at Min")

    def temp_max():
        light.set_temperature(6500, 0)
        global single_temp
        single_temp = 6500

    def temp_min():
        light.set_temperature(2200, 0)
        global single_temp
        single_temp = 2200

    def dim():
        old_on, old_lum, old_temp, old_r, old_g, old_b = gateway.update_light_status(light)
        global single_level
        if old_lum > 20:
            for i in range(old_lum, old_lum - 20, -5):
                light.set_luminance(i, 0)
            single_level = i
            time.sleep(0.5)
        else:
            single_level = old_lum
            print("Already at Min")

    def bright():
        old_on, old_lum, old_temp, old_r, old_g, old_b = gateway.update_light_status(light)
        global single_level
        if old_lum < 100:
            for i in range(old_lum, old_lum + 20, 5):
                light.set_luminance(i, 0)
            single_level = i
            time.sleep(0.5)

        else:
            single_level = old_lum
            print("Already at Max")

    def on():
        light.set_temperature(2500, 0)
        light.set_luminance(100, 0)
        light.set_onoff(1)

    def off():
        light.set_onoff(0)

    def color():
        random.choice(SINGLE_COLOR)()

SINGLE_COLOR = [single.red, single.lime, single.blue, single.yellow, single.aqua, single.magenta, single.silver, single.gray, single.maroon, single.olive, single.green, single.purple, single.teal, single.navy]

if args.action == ['on'] and args.group is not None:
    groups.on()
    print(GROUP_NAME, "is now on")
elif args.action == ['on']:
    single.on()
    print(LIGHT1, "is now on")

if args.action == ['off'] and args.group is not None:
    groups.off()
    print(GROUP_NAME, "is now off")
elif args.action == ['off']:
    single.off()
    print(LIGHT1, "light is now off")

if args.action == ['bright'] and args.group is not None:
    groups.bright()
    print(GROUP_NAME, "level is now set to", groups_level)
elif args.action == ['bright']:
    single.bright()
    print(LIGHT1, "level is now set to", single_level)

if args.action == ['dim'] and args.group is not None:
    groups.dim()
    print(GROUP_NAME, "level is now set to", groups_level)
elif args.action == ['dim']:
    single.dim()
    print(LIGHT1, "level is now set to", single_level)

if args.action == ['color'] and args.group is not None:
    groups.color()
    print(GROUP_NAME, "is now", groups.COLOR_CHOICE)
elif args.action == ['color']:
    single.color()
    print(LIGHT1, "is now", single.COLOR_CHOICE)

if args.action == ['temp_up'] and args.group is not None:
    groups.temp_up()
    print(GROUP_NAME, "temp has been raised to", groups_temp)
elif args.action == ['temp_up']:
    single.temp_up()
    print(LIGHT1, "temp has been raised to", single_temp)

if args.action == ['temp_down'] and args.group is not None:
    groups.temp_down()
    print(GROUP_NAME, "temp has been lowered to", groups_temp)
elif args.action == ['temp_down']:
    single.temp_down()
    print(LIGHT1, "temp has been lowered to", single_temp)

if args.action == ['temp_min'] and args.group is not None:
    groups.temp_min()
    print(GROUP_NAME, "is now at minimum levels of", groups_temp)
elif args.action == ['temp_min']:
    single.temp_min()
    print(LIGHT1, "is now at minimum levels of", single_temp)


if args.action == ['temp_max'] and args.group is not None:
    groups.temp_max()
    print(GROUP_NAME, "is now at maximum levels of", groups_temp)

elif args.action == ['temp_max']:
    single.temp_max()
    print(LIGHT1, "is now at maximum levels of", single_temp)

gateway.update_all_light_status()
