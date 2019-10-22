#******************************************************************************#
#                                                                              #
#                                                         ::::::::             #
#    main module                                        :+:    :+:             #
#                                                      +:+                     #
#    By: pacovali <marvin@codam.nl>                   +#+                      #
#                                                    +#+                       #
#    Created: 2019/01/01 00:00:00 by pacovali      #+#    #+#                  #
#    Updated: 2019/01/01 00:00:00 by pacovali      ########   odam.nl          #
#                                                                              #
#******************************************************************************#

import json
import sys
from os.path import realpath
from Machine_class import Machine

if (len(sys.argv) != 3) :
    print ("Error: provide exactly two arguments: unary_sub.json 'input string'");
    exit();

try :
    with open(realpath(__file__)[:-7] + sys.argv[1], "r") as read_file :
        try :
            description = json.load(read_file);
        except :
            print ("Error: '", sys.argv[1], "' is not a valid file");
            exit ();
except :
    print ("Error: file '", sys.argv[1], "' couldn't be open");
    exit ();

mandatory_fields = ["name", "alphabet", "blank", "states",
                             "initial", "finals", "transitions"];
allowed_keywords = ["read", "write", "to_state", "action"];
allowed_actions = ["LEFT", "RIGHT"];

for field in mandatory_fields :
    if field not in description :
        print ("Error: mandatory field '", field, "' is not in machine description", sep='');
        exit();

for final in description['finals'] :
    if final not in description['states']:
        print("Error: final state '", description['finals'], "' is not a valid state", sep='');
        exit();

for state in description['states'] :
    if state not in description['transitions'] and state not in description['finals'] :
        print ("Error: mandatory state '", state, "' is not described", sep='');
        exit();
    if state not in description['finals'] :
        for details in description['transitions'][state]:
            for keyword in allowed_keywords:
                if keyword not in details:
                    print("Error: state detalisation '", details, "' is missing keyword'", keyword, sep='');
                    exit();
            if details['read'] not in description['alphabet'] \
                    or details['write'] not in description['alphabet']:
                print("Error: state detalisation '", details, "' contains forbidden character", sep='');
                exit();
            if details['to_state'] not in description['states']:
                print("Error: state detalisation '", details, "' contains forbidden state switch", sep='');
                exit();
            if details['action'] not in allowed_actions:
                print("Error: state detalisation '", details, "' contains forbidden action", sep='');
                exit();

for c in sys.argv[2] :
    if c not in description['alphabet'] :
        print("Error: character '", c, "' from user input is not allowed", sep='');
        exit();

machine = Machine(description, sys.argv[2]);
machine.execute();
