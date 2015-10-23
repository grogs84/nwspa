

print '\n'
# probability of withdrawl and check balance
pw = .93
pb = .32
print "p(w) = {}".format(pw)
print "p(b) = {}".format(pb)
print '\n'

# probability of using ATM and not withdrawling
# and probability of not checking balance
npw = 1-pw
npb = 1-pb
print "p(w') = {}".format(npw)
print "p(b') = {}".format(npb)
print '\n'
# probability of using ATM to withdrawl or check balance
pw_or_pb = .96

# probability of checking balance and withdrawling
# p(A & B) = P(A) + P(B) - P(A or B)
print "p(A & B) = P(A) + P(B) - P(A or B)"
print "p(w & b) = P(w) + p(b) - P(w or b)"
pw_a_pb = pw + pb - pw_or_pb
print "p(w & b) = {}".format(pw_a_pb)
print '\n'

# P(B|A) = P(A & B)/P(A)
print "P(B|A) = P(A & B)/P(A)"
print "P(b|w) = p(w & b)/P(w)"
pb_given_w = float(pw_a_pb) / pw
print "P(b|w) = {}".format(pb_given_w)
print '\n'

# P(b|w') = 1 - P(b|w)
print "P(b|w') = 1 - P(b|w)"
pb_given_nw = 1.0 - pb_given_w
print "P(b|w') = {}".format(pb_given_nw)
print '\n'

print "P(A|B) = P(A)*P(B|A)/ P(A)*(B|A) + P(A')*P(B|A')"
print "P(w|b) = P(w)*P(b|w)/ P(w)*P(b|w)+ P(w')*P(b|w')"

pw_given_b = float(pw*pb_given_nw)/((pw*pb_given_nw)+(npw*pb_given_nw))
print "P(w|b) = {}".format(pw_given_b)