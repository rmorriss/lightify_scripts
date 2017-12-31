from lightify import Lightify

# the group should contain at least two lights

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
group.set_onoff(0)
gateway.update_all_light_status()