inst = input()
output = ""

for i in range(len(inst)):
  if inst[i].isalpha():
    output += inst[i]
  elif inst[i] == '+':
    output += " tighten "
  elif inst[i] == '-':
    output += " loosen "
  else:
    output += inst[i]
    if not i == len(inst) - 1 and inst[i+1].isalpha():
      output += "\n"

print(output)


    # string input;
    # cin >> input;

    # string op;

    # for (int i=0; i<input.length(); i++){
    #     if (input[i]>='A' && input[i]<='Z'){
    #          op += input[i];
    #     }

    #     else if (input[i]=='+' || input[i]=='-'){
    #         if (input[i]=='+') op += " tighten ";
    #         else op += " loosen ";
    #     }

    #     else{
    #         if (!(input[i+1]>='A')) op += input[i];
    #         else{
    #             op += input[i];
    #             op += '\n';
    #         }
    #     } 
    # }

    # cout << op << endl;