import misc_tools
import random

def create_routing(env, first_step='op5'):


## if you have a problem with one of the values,
## just update outside of the tasks dictionary for now
	tasks = {
	
		# note: op5 has move time, but this has not been allocated
		# to the PC yet, it is all done by quality controller
        'op5': misc_tools.make_quality_step(
        	env=env,
        	run_time=1,
        	route_to='op7'
        	)
        'op7': {
        	'location': env['assembly_bench'],
        	'worker': env['assembler'],
        	'manned': True,
        	'setup_time': 0,
        	'run_time': 7.6455,
        	'teardown_time': 0,
        	'transit_time': 0,
        	'route_to': 'op8'
        }
        'op8': {
        	'location': env['common_process'],
        	'worker': env['technician'],
            # this step is an unmanned step --> update appropriately!!
        	'manned': True,
        	'setup_time': 0,
        	'run_time': 1,
        	'teardown_time': 0,
        	'transit_time': 0,
        	'route_to': 'op9'
        }
        'op9': {
        	'location': env['common_process'],
        	'worker': env['technician'],
        	'manned': True,
        	'setup_time': 5,
        	'run_time': 5,
        	'teardown_time': 1,
        	'transit_time': 0,
        	'route_to': env['optx_kanban']
        }
        
	    
    }
    tasks['op5']['setup_time'] = 1
    tasks['op5']['teardown_time']=1

    return misc_tools.make_steps(first_step=first_step, tasks=tasks)

def create_kanban_attrs(env):

	return misc_tools.make_kanban_attrs(order_gen=env['gener.optx'],
										order_point=20, order_qty=50,
										init_qty=50, warmup_time=0)
    # what are the details of this specific kanban?order point, order quantity, etc.
    # because I just made mine up


	