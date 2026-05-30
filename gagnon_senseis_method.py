from calculations.prob_utilities import distributions


# def get_chance_of_ending_by_this_round(total_events_size: int, total_successful_events_size: int, amount_of_trials: int, desired_successful_trials: int):
#         chances_from_previous_steps = distributions.get_hyper_geometric_chances(total_events_size, total_successful_events_size, trials_ran, desired_successful_trials - 1)
#         chances_at_this_step = distributions.get_singular_event_chance(total_successful_events_size - 1 , total_events_size - trials_ran)
#         return chances_from_previous_steps * chances_at_this_step


def push_your_luck_style(total_events_size: int, total_successful_events_size: int, amount_of_trials: int, desired_successful_trials: int):
    sum_of_chances = 0
    trials_ran = 1
    while trials_ran < amount_of_trials:
        # print("total_events_size: " + str(total_events_size))
        # print("total_successful_events_size: " + str(total_successful_events_size))
        # print("amount_of_trials: " + str(amount_of_trials))
        # print("trials_ran: " + str(trials_ran))
        # print("desired_successful_trials: " + str(desired_successful_trials))
        chances_from_previous_steps = distributions.get_hyper_geometric_chances(total_events_size, total_successful_events_size, trials_ran, desired_successful_trials - 1) 
        # print("chances_from_previous_steps: " + str(chances_from_previous_steps))
        chances_at_this_step = distributions.get_singular_event_chance(total_successful_events_size - 1 , total_events_size - trials_ran)
        # print("chances_at_this_step: " + str(chances_at_this_step))
        sum_of_chances = sum_of_chances + chances_from_previous_steps * chances_at_this_step
        # print(sum_of_chances)
        
        trials_ran = trials_ran + 1
    print(sum_of_chances)
    return sum_of_chances