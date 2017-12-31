from lightify import Lightify
import time

# the group should contain at least two lights

GROUP_SLEEP = 3
GATEWAY_ADDR = "192.168.1.13"
LIGHT1 = 'Great Room 01'
GROUP1 = 'Great Room'
GROUP1_LIGHTS = ['Great Room 01', 'Great Room 02', 'Great Room 03', 'Great Room 04', 'Great Room 05', 'Great Room 06', 'Great Room 07', 'Great Room 08', 'Great Room 09', 'Great Room 10', 'Great Room 11', 'Great Room 12']

#def gateway():
gateway = Lightify(GATEWAY_ADDR)
gateway.update_all_light_status()
gateway.update_group_list()

#def off(gateway):
group = gateway.groups()[GROUP1]
lights = ([gateway.lights()[addr] for addr in group.lights()])

gateway.update_all_light_status()
time.sleep(GROUP_SLEEP)
group.set_luminance(100, 0)
time.sleep(GROUP_SLEEP)
group.set_luminance(75, 0)
time.sleep(GROUP_SLEEP)
group.set_luminance(50, 0)
time.sleep(GROUP_SLEEP)
group.set_luminance(25, 0)
time.sleep(GROUP_SLEEP)
group.set_luminance(0, 0)
print set_luminance(old_lum)
#time.sleep(0.1)
#group.set_luminance(50, 2)
#time.sleep(0.1)
#group.set_luminance(40, 2)
#time.sleep(0.1)
#group.set_luminance(30, 2)
#time.sleep(0.1)
#group.set_luminance(20, 2)
#time.sleep(0.1)
#group.set_luminance(10, 2)
#time.sleep(0.1)
#group.set_luminance(0, 0)
gateway.update_all_light_status()