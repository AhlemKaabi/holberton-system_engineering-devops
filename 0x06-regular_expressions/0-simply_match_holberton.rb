#!/usr/bin/env ruby
if ARGV.length != 1
	puts "we need exactly one argument"
	exit
end
pattren = ARGV[0].scan(/Holberton/)
for i in pattren
	print i
end
print"\n"
