

seat_belt = .49
no_seat_belt = .51

seat_belt_injured = .46
seat_belt_killed = .27
seat_belt_unharmed = .27

no_seat_belt_injured = .41
no_seat_belt_killed  = .52
no_seat_belt_unharmed = .07

prob_of_selecting_unharmed_person = seat_belt * seat_belt_unharmed + no_seat_belt*no_seat_belt_unharmed

prob_unharmed_not_wearing_seat_belt = prob_of_selecting_unharmed_person/no_seat_belt

print prob_unharmed_not_wearing_seat_belt