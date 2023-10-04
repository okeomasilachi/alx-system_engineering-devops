#!/usr/bin/env ruby
# exactly matching a string that starts with h ends with n
# and can have any single character in between
puts ARGV[0].scan(/^h.n$/).join
