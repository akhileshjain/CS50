{"filter":false,"title":"dna.py","tooltip":"/pset6/dna/dna.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":10,"column":54},"end":{"row":10,"column":55},"action":"remove","lines":["n"],"id":205},{"start":{"row":10,"column":54},"end":{"row":10,"column":55},"action":"remove","lines":["t"]},{"start":{"row":10,"column":54},"end":{"row":10,"column":55},"action":"remove","lines":["("]}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["1"],"id":206}],[{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["1"],"id":207}],[{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["1"],"id":208}],[{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"remove","lines":["1"],"id":209}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":10},"action":"remove","lines":["reader"],"id":210},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["p"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["D"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["a"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["t"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["a"]}],[{"start":{"row":9,"column":15},"end":{"row":9,"column":21},"action":"remove","lines":["reader"],"id":211},{"start":{"row":9,"column":15},"end":{"row":9,"column":20},"action":"insert","lines":["pData"]}],[{"start":{"row":4,"column":0},"end":{"row":6,"column":0},"action":"remove","lines":["if len(sys.argv) != 3:","    sys.exit(\"Usage: dna.py FILENAME \")",""],"id":212},{"start":{"row":4,"column":0},"end":{"row":6,"column":10},"action":"insert","lines":["if len(argv) < 3:","    print(\"usage error, dna.py sequence.txt database.csv\")","    exit()"]}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":213}],[{"start":{"row":8,"column":0},"end":{"row":11,"column":66},"action":"remove","lines":["with open(sys.argv[1]) as file:","    pData = DictReader(file)","    for row in pData:","        print(row[\"name\"], row[\"AGATC\"], row[\"AATG\"], row[\"TATC\"])"],"id":214},{"start":{"row":8,"column":0},"end":{"row":14,"column":13},"action":"insert","lines":["# extract the sequences from the database into a list","with open(argv[1]) as peoplefile:","    people = reader(peoplefile)","    for row in people:","        dnaSequences = row","        dnaSequences.pop(0)","        break"]}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"insert","lines":["p"],"id":215},{"start":{"row":22,"column":1},"end":{"row":22,"column":2},"action":"insert","lines":["r"]},{"start":{"row":22,"column":2},"end":{"row":22,"column":3},"action":"insert","lines":["i"]},{"start":{"row":22,"column":3},"end":{"row":22,"column":4},"action":"insert","lines":["t"]},{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"insert","lines":["n"]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"remove","lines":["n"],"id":216},{"start":{"row":22,"column":3},"end":{"row":22,"column":4},"action":"remove","lines":["t"]}],[{"start":{"row":22,"column":3},"end":{"row":22,"column":4},"action":"insert","lines":["n"],"id":217},{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":22,"column":5},"end":{"row":22,"column":7},"action":"insert","lines":["()"],"id":218}],[{"start":{"row":22,"column":6},"end":{"row":22,"column":7},"action":"insert","lines":["d"],"id":219},{"start":{"row":22,"column":7},"end":{"row":22,"column":8},"action":"insert","lines":["n"]},{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["a"]},{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["s"]},{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["q"],"id":220},{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["u"]},{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["e"]},{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["n"]},{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["c"]},{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["e"]},{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["s"]}],[{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"remove","lines":["s"],"id":221}],[{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["S"],"id":222}],[{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["s"],"id":223},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":["y"]},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["s"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["."]}],[{"start":{"row":16,"column":10},"end":{"row":16,"column":13},"action":"remove","lines":["sys"],"id":224},{"start":{"row":16,"column":10},"end":{"row":16,"column":11},"action":"remove","lines":["."]}],[{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["s"],"id":225},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["y"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["s"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["."]}],[{"start":{"row":9,"column":14},"end":{"row":9,"column":18},"action":"insert","lines":["team"],"id":226}],[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"remove","lines":["m"],"id":227},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"remove","lines":["a"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"remove","lines":["e"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"remove","lines":["t"]}],[{"start":{"row":16,"column":10},"end":{"row":16,"column":11},"action":"insert","lines":["s"],"id":228},{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"insert","lines":["y"]},{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":["s"]},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":["."]}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":19},"action":"remove","lines":["print(dnaSequences)"],"id":229}],[{"start":{"row":22,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":230},{"start":{"row":23,"column":0},"end":{"row":23,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":23,"column":1},"end":{"row":23,"column":2},"action":"insert","lines":[" "],"id":231},{"start":{"row":23,"column":2},"end":{"row":23,"column":3},"action":"insert","lines":["C"]},{"start":{"row":23,"column":3},"end":{"row":23,"column":4},"action":"insert","lines":["o"]},{"start":{"row":23,"column":4},"end":{"row":23,"column":5},"action":"insert","lines":["p"]},{"start":{"row":23,"column":5},"end":{"row":23,"column":6},"action":"insert","lines":["y"]}],[{"start":{"row":23,"column":6},"end":{"row":23,"column":7},"action":"insert","lines":[" "],"id":232},{"start":{"row":23,"column":7},"end":{"row":23,"column":8},"action":"insert","lines":["i"]},{"start":{"row":23,"column":8},"end":{"row":23,"column":9},"action":"insert","lines":["n"]},{"start":{"row":23,"column":9},"end":{"row":23,"column":10},"action":"insert","lines":["t"]},{"start":{"row":23,"column":10},"end":{"row":23,"column":11},"action":"insert","lines":["o"]}],[{"start":{"row":23,"column":11},"end":{"row":23,"column":12},"action":"insert","lines":[" "],"id":233},{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"insert","lines":["a"]}],[{"start":{"row":23,"column":13},"end":{"row":23,"column":14},"action":"insert","lines":[" "],"id":234},{"start":{"row":23,"column":14},"end":{"row":23,"column":15},"action":"insert","lines":["d"]},{"start":{"row":23,"column":15},"end":{"row":23,"column":16},"action":"insert","lines":["i"]},{"start":{"row":23,"column":16},"end":{"row":23,"column":17},"action":"insert","lines":["c"]},{"start":{"row":23,"column":17},"end":{"row":23,"column":18},"action":"insert","lines":["t"]},{"start":{"row":23,"column":18},"end":{"row":23,"column":19},"action":"insert","lines":["i"]},{"start":{"row":23,"column":19},"end":{"row":23,"column":20},"action":"insert","lines":["o"]},{"start":{"row":23,"column":20},"end":{"row":23,"column":21},"action":"insert","lines":["n"]},{"start":{"row":23,"column":21},"end":{"row":23,"column":22},"action":"insert","lines":["a"]},{"start":{"row":23,"column":22},"end":{"row":23,"column":23},"action":"insert","lines":["l"]}],[{"start":{"row":23,"column":22},"end":{"row":23,"column":23},"action":"remove","lines":["l"],"id":235}],[{"start":{"row":23,"column":22},"end":{"row":23,"column":23},"action":"insert","lines":["r"],"id":236},{"start":{"row":23,"column":23},"end":{"row":23,"column":24},"action":"insert","lines":["y"]}],[{"start":{"row":23,"column":24},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":237}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":1},"action":"insert","lines":["f"],"id":238},{"start":{"row":24,"column":1},"end":{"row":24,"column":2},"action":"insert","lines":["o"]},{"start":{"row":24,"column":2},"end":{"row":24,"column":3},"action":"insert","lines":["r"]}],[{"start":{"row":24,"column":3},"end":{"row":24,"column":4},"action":"insert","lines":[" "],"id":239},{"start":{"row":24,"column":4},"end":{"row":24,"column":5},"action":"insert","lines":["i"]},{"start":{"row":24,"column":5},"end":{"row":24,"column":6},"action":"insert","lines":["t"]},{"start":{"row":24,"column":6},"end":{"row":24,"column":7},"action":"insert","lines":["e"]},{"start":{"row":24,"column":7},"end":{"row":24,"column":8},"action":"insert","lines":["m"]}],[{"start":{"row":24,"column":8},"end":{"row":24,"column":9},"action":"insert","lines":[" "],"id":240},{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"insert","lines":["i"]},{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"insert","lines":["n"]}],[{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":[" "],"id":241},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["d"]},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":["n"]},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"insert","lines":["a"]},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":["S"]},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["w"]}],[{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"remove","lines":["w"],"id":242}],[{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["e"],"id":243}],[{"start":{"row":24,"column":12},"end":{"row":24,"column":17},"action":"remove","lines":["dnaSe"],"id":244},{"start":{"row":24,"column":12},"end":{"row":24,"column":24},"action":"insert","lines":["dnaSequences"]}],[{"start":{"row":24,"column":24},"end":{"row":24,"column":25},"action":"insert","lines":[":"],"id":245}],[{"start":{"row":24,"column":25},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":246},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":["s"],"id":247},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"insert","lines":["e"]},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"insert","lines":["q"]},{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":["u"]},{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["e"]},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["n"]},{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":["c"]}],[{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"insert","lines":["e"],"id":248},{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":["s"]},{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"insert","lines":["p"]},{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"insert","lines":["i"]},{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["t"]},{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"insert","lines":["e"]},{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"insert","lines":["m"]}],[{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"remove","lines":["m"],"id":249},{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"remove","lines":["e"]},{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"remove","lines":["t"]},{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"remove","lines":["i"]},{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"remove","lines":["p"]}],[{"start":{"row":25,"column":13},"end":{"row":25,"column":15},"action":"insert","lines":["[]"],"id":250}],[{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"insert","lines":["i"],"id":251},{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["t"]},{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"insert","lines":["e"]},{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"insert","lines":["m"]}],[{"start":{"row":25,"column":19},"end":{"row":25,"column":20},"action":"insert","lines":[" "],"id":252},{"start":{"row":25,"column":20},"end":{"row":25,"column":21},"action":"insert","lines":["="]}],[{"start":{"row":25,"column":21},"end":{"row":25,"column":22},"action":"insert","lines":[" "],"id":253}],[{"start":{"row":25,"column":22},"end":{"row":25,"column":23},"action":"insert","lines":["1"],"id":254}],[{"start":{"row":25,"column":23},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":255},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"remove","lines":["    "],"id":256}],[{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":257},{"start":{"row":27,"column":0},"end":{"row":27,"column":1},"action":"insert","lines":["f"]},{"start":{"row":27,"column":1},"end":{"row":27,"column":2},"action":"insert","lines":["o"]},{"start":{"row":27,"column":2},"end":{"row":27,"column":3},"action":"insert","lines":["r"]}],[{"start":{"row":27,"column":3},"end":{"row":27,"column":4},"action":"insert","lines":[" "],"id":258},{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["i"]}],[{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":[" "],"id":259},{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["i"]},{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"insert","lines":["n"]}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":[" "],"id":260},{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"insert","lines":["s"]},{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"insert","lines":["e"]},{"start":{"row":27,"column":11},"end":{"row":27,"column":12},"action":"insert","lines":["q"]},{"start":{"row":27,"column":12},"end":{"row":27,"column":13},"action":"insert","lines":["u"]},{"start":{"row":27,"column":13},"end":{"row":27,"column":14},"action":"insert","lines":["e"]},{"start":{"row":27,"column":14},"end":{"row":27,"column":15},"action":"insert","lines":["n"]},{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"insert","lines":["c"]}],[{"start":{"row":27,"column":16},"end":{"row":27,"column":17},"action":"insert","lines":["e"],"id":261},{"start":{"row":27,"column":17},"end":{"row":27,"column":18},"action":"insert","lines":["s"]},{"start":{"row":27,"column":18},"end":{"row":27,"column":19},"action":"insert","lines":[":"]}],[{"start":{"row":27,"column":19},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":262},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"remove","lines":["i"],"id":263},{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["k"]},{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":["w"]},{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["y"]}],[{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"remove","lines":["y"],"id":264},{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"remove","lines":["w"]}],[{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":["e"],"id":265},{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["y"]}],[{"start":{"row":28,"column":4},"end":{"row":28,"column":5},"action":"insert","lines":["l"],"id":266}],[{"start":{"row":28,"column":5},"end":{"row":28,"column":6},"action":"insert","lines":[" "],"id":267},{"start":{"row":28,"column":6},"end":{"row":28,"column":7},"action":"insert","lines":["="]}],[{"start":{"row":28,"column":7},"end":{"row":28,"column":8},"action":"insert","lines":[" "],"id":268},{"start":{"row":28,"column":8},"end":{"row":28,"column":9},"action":"insert","lines":["l"]},{"start":{"row":28,"column":9},"end":{"row":28,"column":10},"action":"insert","lines":["e"]},{"start":{"row":28,"column":10},"end":{"row":28,"column":11},"action":"insert","lines":["n"]}],[{"start":{"row":28,"column":11},"end":{"row":28,"column":13},"action":"insert","lines":["()"],"id":269}],[{"start":{"row":28,"column":12},"end":{"row":28,"column":13},"action":"insert","lines":["j"],"id":270}],[{"start":{"row":28,"column":12},"end":{"row":28,"column":13},"action":"remove","lines":["j"],"id":271}],[{"start":{"row":28,"column":12},"end":{"row":28,"column":13},"action":"insert","lines":["k"],"id":272},{"start":{"row":28,"column":13},"end":{"row":28,"column":14},"action":"insert","lines":["e"]},{"start":{"row":28,"column":14},"end":{"row":28,"column":15},"action":"insert","lines":["y"]}],[{"start":{"row":28,"column":16},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":273},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":5},"action":"insert","lines":["t"],"id":274},{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"insert","lines":["m"]}],[{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"remove","lines":["m"],"id":275}],[{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"insert","lines":["e"],"id":276},{"start":{"row":29,"column":6},"end":{"row":29,"column":7},"action":"insert","lines":["m"]},{"start":{"row":29,"column":7},"end":{"row":29,"column":8},"action":"insert","lines":["o"]}],[{"start":{"row":29,"column":8},"end":{"row":29,"column":9},"action":"insert","lines":[" "],"id":277}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":9},"action":"remove","lines":["temo "],"id":278},{"start":{"row":29,"column":4},"end":{"row":30,"column":12},"action":"insert","lines":["tempMax = 0","    temp = 0"]}],[{"start":{"row":30,"column":12},"end":{"row":31,"column":0},"action":"insert","lines":["",""],"id":279},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":31,"column":4},"end":{"row":31,"column":29},"action":"insert","lines":["for i in range(len(dna)):"],"id":280}],[{"start":{"row":31,"column":29},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":281},{"start":{"row":32,"column":0},"end":{"row":32,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":32,"column":8},"end":{"row":32,"column":9},"action":"insert","lines":["w"],"id":282},{"start":{"row":32,"column":9},"end":{"row":32,"column":10},"action":"insert","lines":["h"]},{"start":{"row":32,"column":10},"end":{"row":32,"column":11},"action":"insert","lines":["i"]},{"start":{"row":32,"column":11},"end":{"row":32,"column":12},"action":"insert","lines":["l"]},{"start":{"row":32,"column":12},"end":{"row":32,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":32,"column":13},"end":{"row":32,"column":14},"action":"insert","lines":[" "],"id":283}],[{"start":{"row":32,"column":14},"end":{"row":32,"column":15},"action":"insert","lines":["t"],"id":284},{"start":{"row":32,"column":15},"end":{"row":32,"column":16},"action":"insert","lines":["e"]},{"start":{"row":32,"column":16},"end":{"row":32,"column":17},"action":"insert","lines":["m"]},{"start":{"row":32,"column":17},"end":{"row":32,"column":18},"action":"insert","lines":["p"]}],[{"start":{"row":32,"column":18},"end":{"row":32,"column":19},"action":"insert","lines":[" "],"id":285},{"start":{"row":32,"column":19},"end":{"row":32,"column":20},"action":"insert","lines":[">"]}],[{"start":{"row":32,"column":20},"end":{"row":32,"column":21},"action":"insert","lines":[" "],"id":286},{"start":{"row":32,"column":21},"end":{"row":32,"column":22},"action":"insert","lines":["0"]},{"start":{"row":32,"column":22},"end":{"row":32,"column":23},"action":"insert","lines":[":"]}],[{"start":{"row":32,"column":23},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":287},{"start":{"row":33,"column":0},"end":{"row":33,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":33,"column":12},"end":{"row":33,"column":13},"action":"insert","lines":["t"],"id":288},{"start":{"row":33,"column":13},"end":{"row":33,"column":14},"action":"insert","lines":["e"]},{"start":{"row":33,"column":14},"end":{"row":33,"column":15},"action":"insert","lines":["m"]},{"start":{"row":33,"column":15},"end":{"row":33,"column":16},"action":"insert","lines":["p"]}],[{"start":{"row":33,"column":16},"end":{"row":33,"column":17},"action":"insert","lines":[" "],"id":289},{"start":{"row":33,"column":17},"end":{"row":33,"column":18},"action":"insert","lines":["="]}],[{"start":{"row":33,"column":18},"end":{"row":33,"column":19},"action":"insert","lines":[" "],"id":290},{"start":{"row":33,"column":19},"end":{"row":33,"column":20},"action":"insert","lines":["t"]},{"start":{"row":33,"column":20},"end":{"row":33,"column":21},"action":"insert","lines":["e"]},{"start":{"row":33,"column":21},"end":{"row":33,"column":22},"action":"insert","lines":["m"]},{"start":{"row":33,"column":22},"end":{"row":33,"column":23},"action":"insert","lines":["p"]}],[{"start":{"row":33,"column":23},"end":{"row":33,"column":24},"action":"insert","lines":[" "],"id":291},{"start":{"row":33,"column":24},"end":{"row":33,"column":25},"action":"insert","lines":["-"]}],[{"start":{"row":33,"column":25},"end":{"row":33,"column":26},"action":"insert","lines":[" "],"id":292},{"start":{"row":33,"column":26},"end":{"row":33,"column":27},"action":"insert","lines":["1"]},{"start":{"row":33,"column":27},"end":{"row":33,"column":28},"action":"insert","lines":[";"]}],[{"start":{"row":33,"column":27},"end":{"row":33,"column":28},"action":"remove","lines":[";"],"id":293}],[{"start":{"row":33,"column":27},"end":{"row":33,"column":28},"action":"insert","lines":["c"],"id":294},{"start":{"row":33,"column":28},"end":{"row":33,"column":29},"action":"insert","lines":["o"]},{"start":{"row":33,"column":29},"end":{"row":33,"column":30},"action":"insert","lines":["n"]}],[{"start":{"row":33,"column":29},"end":{"row":33,"column":30},"action":"remove","lines":["n"],"id":295},{"start":{"row":33,"column":28},"end":{"row":33,"column":29},"action":"remove","lines":["o"]},{"start":{"row":33,"column":27},"end":{"row":33,"column":28},"action":"remove","lines":["c"]}],[{"start":{"row":33,"column":27},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":296},{"start":{"row":34,"column":0},"end":{"row":34,"column":12},"action":"insert","lines":["            "]},{"start":{"row":34,"column":12},"end":{"row":34,"column":13},"action":"insert","lines":["c"]},{"start":{"row":34,"column":13},"end":{"row":34,"column":14},"action":"insert","lines":["o"]},{"start":{"row":34,"column":14},"end":{"row":34,"column":15},"action":"insert","lines":["n"]},{"start":{"row":34,"column":15},"end":{"row":34,"column":16},"action":"insert","lines":["t"]},{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"insert","lines":["r"]},{"start":{"row":34,"column":17},"end":{"row":34,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":34,"column":17},"end":{"row":34,"column":18},"action":"remove","lines":["n"],"id":297},{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"remove","lines":["r"]}],[{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"insert","lines":["o"],"id":298},{"start":{"row":34,"column":17},"end":{"row":34,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":34,"column":17},"end":{"row":34,"column":18},"action":"remove","lines":["n"],"id":299},{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"remove","lines":["o"]}],[{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"insert","lines":["i"],"id":300},{"start":{"row":34,"column":17},"end":{"row":34,"column":18},"action":"insert","lines":["n"]},{"start":{"row":34,"column":18},"end":{"row":34,"column":19},"action":"insert","lines":["u"]},{"start":{"row":34,"column":19},"end":{"row":34,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":34,"column":20},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":301},{"start":{"row":35,"column":0},"end":{"row":35,"column":12},"action":"insert","lines":["            "]},{"start":{"row":35,"column":8},"end":{"row":35,"column":12},"action":"remove","lines":["    "]}],[{"start":{"row":35,"column":8},"end":{"row":42,"column":30},"action":"insert","lines":["if dna[i: i + l] == key:","            while dna[i - l: i] == dna[i: i + l]:","                temp += 1","                i += l","","            # it compares the value to the previous longest sequence and if it is longer it overrides it","            if temp > tempMax:","                tempMax = temp"],"id":302}],[{"start":{"row":34,"column":20},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":303},{"start":{"row":35,"column":0},"end":{"row":35,"column":12},"action":"insert","lines":["            "]},{"start":{"row":35,"column":8},"end":{"row":35,"column":12},"action":"remove","lines":["    "]}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"remove","lines":["    "],"id":304},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"remove","lines":["    "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":0,"column":0},"end":{"row":43,"column":26},"action":"remove","lines":["from csv import reader, DictReader","import sys","","# Ensure correct usage","if len(sys.argv) < 3:","    print(\"usage error, dna.py sequence.txt database.csv\")","    exit()","","# extract the sequences from the database into a list","with open(sys.argv[1]) as peoplefile:","    people = reader(peoplefile)","    for row in people:","        dnaSequences = row","        dnaSequences.pop(0)","        break","","with open(sys.argv[2]) as file:","    reader1 = reader(file)","    for row in reader1:","        dnareader = row","","dnaseq = dnareader[0]","","# Copy into a dictionary","for item in dnaSequences:","    sequences[item] = 1","","for key in sequences:","    l = len(key)","    tempMax = 0","    temp = 0","    for i in range(len(dna)):","        while temp > 0:","            temp = temp - 1","            continue","        ","        if dna[i: i + l] == key:","            while dna[i - l: i] == dna[i: i + l]:","                temp += 1","                i += l","","        # it compares the value to the previous longest sequence and if it is longer it overrides it","        if temp > tempMax:","            tempMax = temp"],"id":305},{"start":{"row":0,"column":0},"end":{"row":67,"column":21},"action":"insert","lines":["from csv import reader, DictReader","from sys import argv","","if len(argv) < 3:","    print(\"usage error, dna.py sequence.txt database.csv\")","    exit()","","# read the dna sequence from the file","with open(argv[2]) as dnafile:","    dnareader = reader(dnafile)","    for row in dnareader:","        dnalist = row","","# store it in a string","dna = dnalist[0]","# create a dictionary where we will store the sequences we intend to count","sequences = {}","","# extract the sequences from the database into a list","with open(argv[1]) as peoplefile:","    people = reader(peoplefile)","    for row in people:","        dnaSequences = row","        dnaSequences.pop(0)","        break","","# copy the list in a dictionary where the genes are the keys","for item in dnaSequences:","    sequences[item] = 1","","# iterate trough the dna sequence, when it finds repetitions of the values from sequence dictionary it counts them","for key in sequences:","    l = len(key)","    tempMax = 0","    temp = 0","    for i in range(len(dna)):","        # after having counted a sequence it skips at the end of it to avoid counting again","        while temp > 0:","            temp -= 1","            continue","","        # if the segment of dna corresponds to the key and there is a repetition of it we start counting","        if dna[i: i + l] == key:","            while dna[i - l: i] == dna[i: i + l]:","                temp += 1","                i += l","","            # it compares the value to the previous longest sequence and if it is longer it overrides it","            if temp > tempMax:","                tempMax = temp","","    # store the longest sequences in the dictionary using the correspondent key","    sequences[key] += tempMax","","# open and iterate trough the database of people treating each one like a dictionary so it can compare to the sequences one","with open(argv[1], newline='') as peoplefile:","    people = DictReader(peoplefile)","    for person in people:","        match = 0","        # compares the sequences to every person and prints name before leaving the program if there is a match","        for dna in sequences:","            if sequences[dna] == int(person[dna]):","                match += 1","        if match == len(sequences):","            print(person['name'])","            exit()","","    print(\"No match\")"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":21},"end":{"row":11,"column":21},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1609757111758,"hash":"5f2183d29c32318527c316c5d4aef5c7efb88e67"}