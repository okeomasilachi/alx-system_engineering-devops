#!/usr/bin/env ruby
# matches the string hbt{from 2 to 5 times}n
puts ARGV[0].scan(/hbt{2,5}n/).join
