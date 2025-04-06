"""
This example shows how to use the timer module from vallog
"""

import vallog as vl

debug = vl.Logger()

# handle timer with instances of the Timer class
timer = vl.Timer()
timer.start_timer()
sum(range(1000000))
result = timer.stop_timer()
debug.log(f"elapsed time: {result}", vl.info)

# handle timer as a context manager
with vl.Timer() as timer:
    sum(range(1000000))

debug.log(f"elapsed time: {timer.elapsed_time}", vl.info)
