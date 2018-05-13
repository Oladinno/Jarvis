from JarvisYacc import parser
import JarvisTools as JT
from JarvisYacc import find_bot
from JarvisYacc import thebots
import sys


def print_message():
    print("Welcome to JARVIS, where you create your own personal assistant!\n")
    print('''                                                          @(((((((((((((((((((((((((((((((((@                                                                  
                                                          @(((((((((((((((((((((((((((((((((@                                                                  
                                                          @(((((((((((((((((((((((((((((((((@                                                                  
                                                          @(((((((((((((((((((((((((((((((((@                                                                  
                                                          @(((((((((((((((((((((((((((((((((@                                                                  
                                                          @(((((((((((((((((((((((((((((((((@                                                                  
                                                          @(((((((((((((((((((((((((((((((((@@%                                                              
                                                   #@(((((@(((((((((((((((((((((((((((((((((@((((((((#@                                                        
                                                @(((((((((@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,&((((((((((((@                                                     
                                               @((((((((((@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@((((((((((((((                                                    
                                                #(((((((((((((((((((((((((((((((((((((((((((((((((((((((((@                                                    
                                                  @%(((((((((((((((((((((((((((((((((((((((((((((((((((@                                                       
                                                    (((@@#(((((((((((((((((((((((((((((((((((((((@@(((&                                                        
                                                  @(((((((((((((((%@@@@@@@@@@@@@@@@@@@@&(((((((((((((((@                                                       
                                                 @((((((((((((((((((((((((((((((((((((((((((((((((((((((@                                                      
                                                @((((((((((((((((((((((((((((((((((((((((((((((((((((((((@                                                     
                                     @(((((((((%(((((((((((((((@.......@(((((((((((@.......@((((((((((((((@((((((((                                            
                                     ((((((((((#((((((((((((((..%(((((...(((((((((..@((((&...((((((((((((((((((((((                                            
                                     (((((((((@((((((((((((((@..(((((((..@(((((((/.*(((((((..@(((((((((((((@(((((((                                            
                       @..@          (((((((((@((((((((((((((%..(((((((..%(((((((..*(((((((..@(((((((((((((&(((((((           @..@                                 
                       @..%%%%%%%%%%%(((((((((#((((((((((((((@...#(((@...@(((((((@../((((@...#(((((((((((((((((((((%%%%%%%%%%%%..@                             
                       @..@          (((((((((((((((((((((((((&.........#(((((((((@.........#((((((((((((((((((((((           @..@                              
                                     (((((((((#((((((((((((((((((@@/@@(@*  @@(@   @((@%*&@(((((((((((((((((((((((((                                            
                                     (((((((((@((((((((((((((((((((((@               @(((((((((((((((((((((%(((((((                                            
                                     (((((((((@((((((((((((((((((((@                   @(((((((((((((((((((@(((((((                                            
                                     (((((((((((((((((((((((@((((@                        @@%@(((((((((((((@@@@@@@@                                            
                                               %((((((((((((((#                           @(((((((((((((((@                                                    
                                                @((((((((((((((((@%,,%@@@@@@((@* ,@%,%@#(((((((((((((((((@                                                     
                                                 @((((((((((((((((((((((((((((((((((((((((((((((((((((((&                                                      
                                                  @((((((((((((((((((((((((((((((((((((((((((((((((((((@                                                       
                                                   #((((((((((@.....@.....@.....%.....@.....((((((((((@                                                        
                                                     @((((((((@.....@.....@.....%.....@.....((((((((&                                                          
                                                       &((((((@.....@.....@.....%.....@.....(((((((                                                            
                                                         @((((@.....@.....@.....%.....@.....((((@                                                              
                                                           *&(@.....@.....@.....%.....@.....(#&                                                                
                                                               @....@.....@.....%.....@...@                                                                    
                                                             ,,     @@....@.....%...&@     %@@%%,                                                              
                                                     &((((((((((((((@                 @(((((((((((((((                                                         
                                                    %(((((((((((((((((@             @(((((((((((((((((@                                                        
                                                    @((((((((((((((((((@(((((((((((@(((((((((((((((((((                                                        
                                                    (((((((((((((((((@(@(((((((((((@%((((((((((((((((((@                                                       
                                                   %(((((((((((((((((((@(((((((((((@(((((((((((((((((((@                                                       
                                                   .(((((((((((((((((((@(((((((((((@(((((((((((((((((((@                                                       
                                                    #((((((((((((((((((@(((((((((((@(((((((((((((((((((                                                        
                                                    @(((((((((((((((((#*,,,,,,,,,,, @(((((((((((((((((@                                                        
                                                     ((((((((((((((@                   &@(((((((((((((                                                         
                                                                                                                                                               


         
    ''')
    print("To run a command, please specify the bot you want to call followed by a comma")
    print("and then type the command you want to run.\n")
    print("If you want to see the available commands that each bot has, just type the bot's")
    print("name without a comma.")
    print("The system's current available bots are:\n")
    for bot in thebots:
        print("-" + bot.name)
    print("\n")
def run_program(name):

    code = ""
    with open(name + '.jvs', 'r') as test:
        for l in test:
            code = code + l
        #print(code)
        parser.parse(code)

    print_message()

    l=""
    while not(l.lower() == "quit"):
        l = str(input(">> "))
        if l != "quit":
            name_until = l.find(',')
            if name_until != -1:
                bot_name = l[:name_until]
                bot = find_bot(bot_name)
                if not bot:
                    print("Bot " + bot_name + " was not created.")
                else:
                    r = bot.handleInput(l[name_until+2:])
            else:
                bot = find_bot(l)
                if not bot:
                    print("Bot " + l + " was not created.")
                else:
                    for rule in bot.rules.keys():
                        print (rule)


if __name__ == "__main__":
    name = sys.argv[1]
    run_program(name)