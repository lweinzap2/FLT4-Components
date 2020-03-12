{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import misc_tools\n",
    "import random\n",
    "\n",
    "def create_routing(env, first_step = 'op_10'):\n",
    "    \n",
    "    tasks = {\n",
    "        'op_10': { # I think this step is wrong? Vsdx file says this is assembly, but it's called 'multiplixer debug'\n",
    "            'location': env['assembly_bench'],\n",
    "            'worker': env['technician'],\n",
    "            'manned': True,\n",
    "            'run_time': ,\n",
    "            'setup_time': 0.5,\n",
    "            'teardown_time': 0.5,\n",
    "            'transit_time': 0,\n",
    "            'route_to': 'op_11'\n",
    "        }\n",
    "        'op_11': { # not sure if the location is correct here, step is called \"Inspect SIP\"\n",
    "            'location': env['assembly_bench'],\n",
    "            'worker': env['inspection'],\n",
    "            'manned': True,\n",
    "            'setup_time': 1,\n",
    "            'run_time': random.gauss(mu=1, sigma=0.1),\n",
    "            'teardown_time': 1,\n",
    "            'transit_time': 1, # do we need transit_time if we have a move step?\n",
    "            'route_to': 'move11'\n",
    "        }\n",
    "        'move11'{\n",
    "            'location': env[''],\n",
    "            'worker': 'prod_control',\n",
    "            'manned': True,\n",
    "            'setup_time': 0,\n",
    "            'run_time': 1,\n",
    "            'teardown_time': 0,\n",
    "            'route_to': 'op_13'\n",
    "        }\n",
    "        'op_13': { # worker is \"automated optical inspection\"?\n",
    "            'location': env['BFPD_CTI'],\n",
    "            'manned': False,\n",
    "            'setup_time': 0,\n",
    "            'run_time': 1,\n",
    "            'route_to': 'op_23'\n",
    "        }\n",
    "        \n",
    "        return misc_tools.make_steps(first_step=first_step, tasks=tasks)\n",
    "    }\n",
    "\n",
    "def create_kanban_attrs(env):\n",
    "\n",
    "    # Quantities need to be assigned here, this is just copied from part_a.py in Jack's example\n",
    "    \n",
    "    return misc_tools.make_kanban_attrs(order_gen=env['gener.BFPD'],\n",
    "                                        order_point=2, order_qty=5,\n",
    "                                        init_qty=5, warmup_time=0)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
