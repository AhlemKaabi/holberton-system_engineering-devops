#!/usr/bin/env ruby
if ARGV.length != 1
	puts "we need exactly one argument"
	exit
end
puts ARGV[0].match(/hbt+n/)