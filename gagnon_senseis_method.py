from calculations.probability import Distributions

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def push_your_luck_style(total_events_size: int, total_successful_events_size: int, amount_of_trials: int, desired_successful_trials: int):
    sum_of_chances = 0
    trials_ran = 0
    desired_successful_trials_at_this_step = 0
    while trials_ran < amount_of_trials:
        chances_from_previous_steps = 0
        if trials_ran > 0:
            chances_from_previous_steps = Distributions.get_hyper_geometric_chances(total_events_size, total_successful_events_size, trials_ran, desired_successful_trials - 1)
        logger.debug(f"trials ran: {trials_ran}")
        chances_at_this_step = (total_successful_events_size - 1) / (total_events_size - trials_ran)
        sum_of_chances = sum_of_chances + chances_from_previous_steps * chances_at_this_step
        trials_ran = trials_ran + 1
    return sum_of_chances