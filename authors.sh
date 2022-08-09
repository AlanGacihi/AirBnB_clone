#!/bin/bash

# generate AUTHORS, modify .mailmap in case of duplicates
git log --reverse --format='%aN <%aE>' | perl -we '
BEGIN {
  %seen = (), @authors = ();
}
while (<>) {
  next if $seen{$_};
  $seen{$_} = push @authors, $_;
}
END {
  print "# Authors ordered by first contribution.\n";
  print "\n", @authors, "\n";
}
' > "AUTHORS"
