#!/usr/bin/env ruby
# searches for the pattern hbtn where b is optional
puts ARGV[0].scan(/hb?tn/).join
