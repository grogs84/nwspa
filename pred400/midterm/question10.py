

seat_belt = .49
no_seat_belt = .51

seat_belt_injured = .46
seat_belt_killed = .27
seat_belt_unharmed = .27

no_seat_belt_injured = .41
no_seat_belt_killed  = .52
no_seat_belt_unharmed = .07

pct_unharmed_w_sb = seat_belt*seat_belt_unharmed
pct_unharmed_wo_sb = no_seat_belt*no_seat_belt_unharmed

prob_unharmed = pct_unharmed_wo_sb+pct_unharmed_w_sb
print 'The probability of selecting an unharmed person from a fatal crash:'
print prob_unharmed

prob_unharmed_wo_sb = pct_unharmed_wo_sb/prob_unharmed
print 'The probability that a randomly selected person who was unharmed in a fatal crash\nwas not wearing a seat belt:'
print prob_unharmed_wo_sb