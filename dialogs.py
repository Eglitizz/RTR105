#!/usr/bin/python
# -*- coding: utf-8 -*-
a = input (" cien. lietotāj, lūdzu ievadiet skaitli: ")
# 3. python'ā visi input rezultāti ir ar str datu tipu
# tapēc ievadītā lieluma datu tips vēlāk ir jāpārveido
a = int(a)

# python valoda balstās uz C valodas=> print strādā līdzīgi printf

print("lietotāj, tu esi ievadījis skaitli: %d"%(a))
aa = a * a
print("Tavs skaitlis kvadrātā ir: %d"%(aa))

