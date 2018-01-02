import time

import pytest

from lightify import Lightify

# adjust these variables according to your installation
# the group should contain at least two lights
GATEWAY_ADDR = "192.168.1.100"
GROUP_SLEEP = 2
LIGHT1 = 'Lightstrip'
GROUP1 = 'bedroom'
GROUP1_LIGHTS = ['Schlafzimmer1', 'Schlafzimmer2']


def colors_almost_equal(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return abs(r1 - r2) <= 2 and abs(g1 - g2) <= 2 and abs(b1 - b2) <= 2


@pytest.fixture(scope="module")
def gateway():
    gateway = Lightify(GATEWAY_ADDR)
    gateway.update_all_light_status()
    gateway.update_group_list()
    return gateway


def test_connection(gateway):
    # tests if a connection is possible and some lights are returned
    print("test_connection")
    assert gateway.lights()


def test_groups(gateway):
    # tests that our group is returned and the lights in it are the same
    # as in GROUP1_LIGHTS
    assert GROUP1 in gateway.groups()
    group = gateway.groups()[GROUP1]
    lights = group.lights()
    light_names = sorted([gateway.lights()[addr].name() for addr in lights])
    assert light_names == sorted(GROUP1_LIGHTS)


def test_group_info(gateway):
    # tests if the function gateway.group_info() returns the lights in
    # GROUP1_LIGHTS
    group = gateway.groups()[GROUP1]
    lights = ([gateway.lights()[addr] for addr in gateway.group_info(group)])
    light_names = sorted([light.name() for light in lights])
    assert light_names == sorted(GROUP1_LIGHTS)


def get_addr_of_light(light_name, gateway):
    for light in gateway.lights().values():
        if light_name == light.name():
            return light
    return None


def test_turn_light_on_and_off(gateway):
    # tests if a light can be turned off, on and off again and the state
    # is updated accordingly
    light = get_addr_of_light(LIGHT1, gateway)
    light.set_onoff(0)
    time.sleep(1)
    assert not light.on()
    light.set_onoff(1)
    time.sleep(1)
    assert light.on()
    light.set_onoff(0)
    time.sleep(1)
    assert not light.on()


def test_turn_group_on_and_off(gateway):
    # tests if a group can be turned off, on and off again
    # and the state of each light in the group is updated accordingly
    group = gateway.groups()[GROUP1]
    lights = ([gateway.lights()[addr] for addr in group.lights()])
    group.set_onoff(0)
    time.sleep(GROUP_SLEEP)
    gateway.update_all_light_status()
    for light in lights:
        assert not light.on()
    group.set_onoff(1)
    time.sleep(GROUP_SLEEP)
    gateway.update_all_light_status()
    for light in lights:
        assert light.on()
    group.set_onoff(0)
    time.sleep(GROUP_SLEEP)
    gateway.update_all_light_status()
    for light in lights:
        assert not light.on()


def test_update_single_light(gateway):
    # test if the update_light_status function updates the on variable
    # correctly when turning the light off, on and off again
    light = get_addr_of_light(LIGHT1, gateway)
    light.set_onoff(0)
    time.sleep(1)
    on, lum, temp, r, g, b = gateway.update_light_status(light)
    assert not on
    assert not light.on()
    light.set_onoff(1)
    time.sleep(1)
    on, lum, temp, r, g, b = gateway.update_light_status(light)
    assert on
    assert light.on()
    light.set_onoff(0)
    time.sleep(1)
    on, lum, temp, r, g, b = gateway.update_light_status(light)
    assert not on
    assert not light.on()


@pytest.mark.skip(reason="requires walking in front of the motion sensor")
def test_motion_sensor(gateway):
    motion_sensor_name = "MotionSensor1"
    motion_sensor = get_addr_of_light(motion_sensor_name, gateway)
    for i in range(1000):
        time.sleep(0.1)
        result = gateway.update_light_status(motion_sensor)
        print(result)


def test_light_by_name(gateway):
    # test if the function light_byname returns the correct light
    light = gateway.light_byname(LIGHT1)
    assert light.name() == LIGHT1


def test_colors_single_light(gateway):
    # switches the light to red, green and blue and checks if the status
    # is updated accordingly
    light = gateway.light_byname(LIGHT1)
    old_on, old_lum, temp, old_r, old_g, old_b = gateway.update_light_status(
        light)

    light.set_onoff(1)
    light.set_luminance(255, 0)
    light.set_rgb(255, 0, 0, 0)
    time.sleep(1)
    on, lum, temp, r, g, b = gateway.update_light_status(light)
    assert colors_almost_equal((r, g, b), (255, 0, 0))

    light.set_rgb(0, 255, 0, 0)
    time.sleep(1)
    on, lum, temp, r, g, b = gateway.update_light_status(light)
    assert colors_almost_equal((r, g, b), (0, 255, 0))

    light.set_rgb(0, 0, 255, 0)
    time.sleep(1)
    on, lum, temp, r, g, b = gateway.update_light_status(light)
    assert colors_almost_equal((r, g, b), (0, 0, 255))

    light.set_rgb(old_r, old_g, old_b, 0)
    light.set_luminance(old_lum, 0)
    light.set_onoff(old_on)


def test_colors_group(gateway):
    # turns the lights in the group to red, then green, then blue and
    # checks if the status is updated accordingly
    group = gateway.groups()[GROUP1]
    lights = ([gateway.lights()[addr] for addr in group.lights()])
    group.set_onoff(1)
    time.sleep(GROUP_SLEEP)
    gateway.update_all_light_status()
    old_rgbs = []
    for light in lights:
        old_rgbs.append(light.rgb())

    group.set_rgb(255, 0, 0, 0)
    time.sleep(GROUP_SLEEP)
    gateway.update_all_light_status()
    for light in lights:
        assert colors_almost_equal(light.rgb(), (255, 0, 0))

    group.set_rgb(0, 255, 0, 0)
    time.sleep(GROUP_SLEEP)
    gateway.update_all_light_status()
    for light in lights:
        assert colors_almost_equal(light.rgb(), (0, 255, 0))

    group.set_rgb(0, 0, 255, 0)
    time.sleep(GROUP_SLEEP)
    gateway.update_all_light_status()
    for light in lights:
        assert colors_almost_equal(light.rgb(), (0, 0, 255))

    for light, old_rgb in zip(lights, old_rgbs):
        r, g, b = old_rgb
        light.set_rgb(r, g, b, 0)


# @pytest.mark.skip(reason="takes very long (about 30s)")
def test_color_cyle(gateway):
    # changes the color of a light in 255 steps and the repeats it once more.
    # this checks if an overflow occurs after 255 steps (was a bug in an older
    # version of python lightify)
    light = gateway.light_byname(LIGHT1)
    old_on, old_lum, temp, old_r, old_g, old_b = gateway.update_light_status(
        light)
    light.set_onoff(1)
    for i in range(512):
        col_val = i % 256
        light.set_rgb(255 - col_val, 255 - col_val, col_val, 0)
        # time.sleep(0.05)
    light.set_rgb(old_r, old_g, old_b, 0)
    light.set_luminance(old_lum, 0)
    light.set_onoff(old_on)


def test_temperature_cyle(gateway):
    # changes the color temperature of a light from 2200 kelvin to 6500
    # in steps of 100.
    light = gateway.light_byname(LIGHT1)
    old_on, old_lum, old_temp, old_r, old_g, old_b = gateway.update_light_status(
        light)
    light.set_onoff(1)
    time.sleep(0.2)
    for i in range(2200, 6501, 100):
        light.set_temperature(i, 0)
        time.sleep(0.1)
    light.set_temperature(old_temp, 0)
    light.set_onoff(old_on)


def test_luminance(gateway):
    # changes the luminance of a light from 0 to 100 in steps of 5
    light = gateway.light_byname(LIGHT1)
    old_on, old_lum, old_temp, old_r, old_g, old_b = gateway.update_light_status(
        light)
    light.set_onoff(1)
    time.sleep(0.2)
    for i in range(0, 101, 5):
        light.set_luminance(i, 0)
        time.sleep(0.1)
    light.set_luminance(old_lum, 0)
    light.set_onoff(old_on)
