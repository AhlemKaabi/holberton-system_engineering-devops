#!/usr/bin/env ruby
if ARGV.length != 1
	puts "we need exactly one argument"
	exit
end
ARGV[0].match(/hb{0,1}tn/)