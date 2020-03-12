
import misc_tools
import random


def create_routing(env, first_step='op1'):
    tasks = {
        'op15': {
            'location': env['assembly_bench'],
            'worker': env['assembler'],
            'manned': manned,
            'setup_time': 1,
            'run_time': 5,
            'teardown_time': 1,
            'transit_time': 1
            'route_to': 'op16'
        },

        'op16': misc_tools.make_quality_step(
            env=env,
            run_time=2,
            route_to='op17',
            transit_time=1
        ),
        'op17': {
            'location': env['machine'],
            'worker': env['technician'],
            'manned': True,
            'setup_time': 1,
            'run_time': 2,
            'teardown_time': 1,
            'transit_time': 1,
            'yeild': 1.00,
            'route_to_pass': env['multiplexer_attempt_kanban'],
        }
    }

    return misc_tools.make_steps(first_step=first_step, tasks=tasks)


def create_kanban_attrs(env):
    return misc_tools.make_kanban_attrs(order_gen=env['gener.splitter_attempt'],
                                        order_point=2, order_qty=5,
                                        init_qty=5, warmup_time=0)

