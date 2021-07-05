#!/usr/bin/env ruby
if ARGV.length != 1
	puts "we need exactly one argument"
	exit
end
ARGV[0].match(hbt{2,5}n)
