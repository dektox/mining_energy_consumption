<template>
    <v-layout justify-center align-center wrap>
    <div style="border: 4px solid red;">
    <h2 style="text-align: center;"><span style="color: #ff0000;">This is a sample page with placeholder text. To see the latest version of the text draft, please visit the "Methodology" section via this link: </span><a href="http://review.cbeci.org">review.cbeci.org</a></h2>
    </div>
        <v-flex xs12 md10 my-3>
            <v-layout justify-center align-center>
                <span style="font-size: 24px">Bitcoin Basics</span>
            </v-layout>
        </v-flex>
        <v-flex xs12 md10 my-3>
            <v-expansion-panel>
                <v-expansion-panel-content
                        v-for="(item,i) in first"
                        :key="i"
                >
                    <template v-slot:header>
                        <div class="qa-title"><b>{{ item.title }}</b></div>
                    </template>
                    <v-card>
                        <v-card-text class="qa-text" v-html="item.text">
                        </v-card-text>
                    </v-card>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-flex>
        <v-flex xs12 md10 my-3>
            <v-layout justify-center align-center>
                <span style="font-size: 24px"><br />Electricity Consumption</span>
            </v-layout>
        </v-flex>
        <v-flex xs12 md10 my-3>
            <v-expansion-panel>
                <v-expansion-panel-content
                        v-for="(item,i) in second"
                        :key="i"
                >
                    <template v-slot:header>
                        <div class="qa-title"><b>{{ item.title }}</b></div>
                    </template>
                    <v-card>
                        <v-card-text class="qa-text" v-html="item.text">
                        </v-card-text>
                    </v-card>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-flex>
        <v-flex xs12 md10 my-3>
            <v-layout justify-center align-center>
                <span style="font-size: 24px"><br />Common Misconceptions</span>
            </v-layout>
        </v-flex>
        <v-flex my-3 xs12 md10>
            <v-expansion-panel style="width: 100%">
                <v-expansion-panel-content
                        v-for="(item,i) in third"
                        :key="i"
                >
                    <template v-slot:header>
                        <div class="qa-title"><b>{{ item.title }}</b></div>
                    </template>
                    <v-card>
                        <v-card-text class="qa-text" v-html="item.text">
                        </v-card-text>
                    </v-card>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-flex>
    </v-layout>
</template>

<script>

    export default {
        name: 'methodology',
        data() {
            return {
                first: [
                    {
                        "title": "What is Bitcoin?",
                        "text": "Bitcoin is a software protocol and peer-to-peer (P2P) network that enables the digital transfer of value globally without relying on trusted intermediaries. Bitcoin is an open and permissionless system: anyone can participate in the network, as well as send, store, and receive payments without having to ask anyone for permission.<br><br>Bitcoin has its own, native cryptocurrency called bitcoin (BTC) which acts as the universal unit of value within the Bitcoin network. New bitcoins are issued, according to a transparent and predictable schedule, every 10 minutes on average through a process called mining. While the Bitcoin protocol specifies that a maximum of 21 million bitcoins will ever be created, it is worth mentioning that one bitcoin can be divided out to eight decimal places. This means that one bitcoin corresponds to 100 million satoshi, the smallest base unit."
                    },
                    {
                        "title": "What is the blockchain?",
                        "text": "All bitcoin transactions are recorded in a public ledger that every node stores locally. The ledger is represented using a particular data structure: transactions are bundled into data blocks, which are then cryptographically linked to each other. This process results in a growing chain of blocks – which is fittingly called the blockchain. The use of this particular data structure ensures that tampering with the transaction history (e.g. modifying past transactions) will be detected immediately by other network participants. The blockchain grows larger every day as new blocks of transactions keep getting added by special participants called miners."
                    },
                    {
                        "title": "What is Proof-of-Work (PoW) mining?",
                        "text": "Imagine Alice has 10 bitcoin that she wants to send to Bob. Shortly after, she changes her mind and suddenly wants to send the same 10 bitcoin to Charlie instead. While both transactions are valid, only one can get processed -- Alice only has 10 bitcoin, not 20 bitcoin! The question now is: in a decentralised system like Bitcoin that has no central authority, who gets to decide which of the two valid but conflicting transactions will get processed?<br><>brEnter PoW mining: instead of simply letting participants vote (and making the vote vulnerable to potential manipulation by attackers creating multiple identities), the idea is to attach a financial cost to the vote. Anyone who wants to participate in the vote (miners) needs to prove that they performed some “work” – hence the term proof-of-work. This work consists of finding the solution to a cryptographic puzzle, which in simple terms can be thought of as simply guessing a random number. The only way of finding the random number -- called a nonce in technical jargon -- is to brute force all possible options. This way, the work cannot be faked but is trivial to verify by other network participants once the winning nonce has been revealed.<br><br>Solving the PoW requires substantial computing power depending on the difficulty level: the more miners join the race, the more difficult the puzzle becomes. Rather than guessing numbers manually, miners operate specialised mining equipment (ASICs) that has been specifically designed to be very good at only one single task -- solving the PoW.<br><br>Miners need to incur financial costs in terms of capital expenditures (acquiring mining hardware) as well as operational expenditures (spending electricity to run and cool the machines). Miners are in constant competition between themselves: whoever finds the solution to the puzzle first obtains the right to add his block to the global ledger. In return, the successful miner gets rewarded for his efforts with newly minted bitcoin. "
                    }
                ],
                second: [
                    {
                        "title": "Why does Bitcoin consume electicity?",
                        "text": "Running mining hardware requires electricity -- and actually quite a bit. The more machines a miner operates, the more likely he is to find the solution to the puzzle. However, more machines also means that more electricity is needed to run and cool the equipment, which in turn results in higher costs for the miner in question. Miners are thus always searching for abundant electricity sources at the lowest possible price.<br><br>While newer ASIC models are substantially more energy-efficient than previous generations, they still consume a significant amount of electricity. Rising bitcoin prices make mining more attractive, as the potential reward increases in value. As a result, new mining hardware will get added to the network and lead to increasing electricity consumption overall."
                    },
                    {
                        "title": "How much electricity does Bitcoin use?",
                        "text": "It is not possible to exactly determine how much electricity Bitcoin uses for a variety of reasons.<br><br>For instance, miners can choose between several ASIC models that often have different energy efficiencies: there is little data available on the exact market share of mining hardware, and miners often reconnect old, less efficient machines when block rewards go up in value. It is difficult to determine what hardware miners are using as profitability may vary significantly from one region to another.<br><br>Moreover, mining operations also require additional electricity to cool the machines to prevent them from overheating, and eventually breaking. Data centres can vary significantly in terms of how efficiently they use electricity: while cooling and overheads for the most efficient facilities account for less than 4% of the electricity used to run hardware, less efficient data centres can use as much electricity for cooling and overheads as is required to simply operate the equipment. It is not possible to exactly determine how efficiently mining facilities use electricity as they are located in different regions and have different configurations and settings.<br><br>The best option is thus to build theoretical models based on specific assumptions (see methodology) to provide an educated guess."
                    },
                    {
                        "title": "What are Bitcoin’s carbon emissions? ",
                        "text": "It is important to understand that energy consumption is not necessarily equivalent to carbon emissions and environmental pollution. For instance, one kilowatt-hour (kWh) of electricity generated by a coal-fired power station has a substantially different environmental footprint than one kWh of electricity produced by solar park.<br><br>In order to determine Bitcoin’s carbon emissions, and thus real environmental footprint, the actual energy mix (i.e. sources of energy used to produce electricity) needs to be examined. While some mining facilities disclose the energy sources used to power their machines, the exact energy mix of the majority of mining farms remains unknown.<br><br>More recently, studies have shown that a growing share of total electricity consumption originates from renewable energy sources such as hydro, solar, and wind power. However, estimates are varying widely, ranging from approximately 20% of the total energy mix to more than 70%."
                    },
                    {
                        "title": "Does this mean Bitcoin boils the oceans?",
                        "text": "There is currently little evidence suggesting that Bitcoin directly contributes to climate change. Even when assuming that Bitcoin mining was exclusively powered by coal -- a very unrealistic scenario, total carbon dioxide emissions would not exceed 58 million tons of CO2, which would roughly correspond to 0.17% of the world’s total carbon emissions.<br><br>This is not to say that environmental concerns regarding Bitcoin’s electricity consumption should be disregarded. There are valid concerns that Bitcoin’s growing electricity consumption may pose a threat to achieving the United Nations Sustainable Development Goals in the future. However, current figures should be put into perspective: available data shows that even in the worst case (mining exclusively powered by coal), Bitcoin’s environmental footprint is currently marginal at best."
                    }
                ],
                third: [
                    {
                        "title": "Energy cost per transaction",
                        "text": "The popular but fallacious energy cost per transaction metric is regularly featured in the news and other outlets despite having multiple issues. In fact, we do not consider it a meaningful metric in the context of PoW blockchains for the following reasons:"
                    },
                    {
                        "title": "Comparing apples to oranges",
                        "text": "Most energy consumption estimates include comparisons with traditional payment systems. This may initially seem appropriate given that Bitcoin is often touted as global payment network. However, a closer look at Bitcoin’s key value proposition reveals the substantial differences between what each system tries to achieve - and as a result the significant divergences in design decisions and requirements."
                    }
                ]
            }
        }
    }
</script>
