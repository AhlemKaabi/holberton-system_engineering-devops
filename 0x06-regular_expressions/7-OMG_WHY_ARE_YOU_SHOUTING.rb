#!/usr/bin/env ruby
if ARGV.length != 1
	puts "we need exactly one argument"
	exit
end
for letter in ARGV[0].scan(/[A-Z]/) do
	print letter
end
print "\n"