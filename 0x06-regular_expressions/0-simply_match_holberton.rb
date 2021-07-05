#!/usr/bin/env ruby
if ARGV.length != 1
	puts "we need exactly one argument"
	exit
end
pattren = ARGV[0].scan(/Holbrton/)
for i in pattren do
	print i
end
print"\n"
