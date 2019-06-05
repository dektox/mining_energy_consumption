<template>
    <v-layout column justify-center align-center>
        <v-flex my-3>
          <span style="font-size: 32px">
            Q&A
          </span>
        </v-flex>
        <v-layout justify-center align-center>
            <v-flex my-3 xs12 md10>
                <v-expansion-panel>
                    <v-expansion-panel-content
                            v-for="(item,i) in items"
                            :key="i"
                    >
                        <template v-slot:header>
                            <div class="qa-title">{{ item.title }}</div>
                        </template>
                        <v-card>
                            <v-card-text class="qa-text" v-html="item.text">
                            </v-card-text>
                        </v-card>
                    </v-expansion-panel-content>
                </v-expansion-panel>
            </v-flex>
        </v-layout>
    </v-layout>
</template>

<script>

    export default {
        name: 'methodology',
        data() {
            return {
                items: [
                    {
                        "title": "What is Bitcoin?",
                        "text": "<b>Bitcoin</b> is a software protocol and peer-to-peer (P2P) network that enables the permissionless digital transfer of value globally without relying on trusted intermediaries. Bitcoin is an open and permissionless system: anyone can participate in the network, as well as send, store, and receive payments without having to ask anyone for permission.<br><br> Bitcoin has its own, native cryptocurrency called <b>bitcoin</b> (BTC). BTC is the digital asset that users can transfer over the network. New bitcoins are issued on average every 10 minutes through a process called <b>mining</b>. While the Bitcoin protocol specifies that a maximum of 21 million bitcoin will ever be created, it is worth mentioning that one bitcoin can be subdivided into 8 decimals: the smallest unit is called a <b>satoshi</b> and corresponds to 0.00000001 BTC."
                    },
                    {
                        "title": "What is the blockchain?",
                        "text": "All bitcoin transactions are recorded in a public ledger that every node stores locally. The ledger is represented using a particular data structure: transactions are bundled into data blocks, which are then cryptographically linked to each other. This process results in a growing chain of blocks – the blockchain. The use of this particular data structure ensures that tampering with the transaction history will be detected immediately by other network participants."
                    },
                    {
                        "title": "What is Proof-of-Work (PoW) mining?",
                        "text": "Imagine Alice has 10 BTC that she wants to send to Bob. Shortly after, she changes her mind and now wants to send the same 10 BTC to Charlie instead. While both transactions are valid, only one can get processed as Alice only has 10 BTC, not 20 BTC. The question now becomes: in a decentralised system like Bitcoin with no central authority, who decides which of the two valid but conflicting transactions will get processed? <br><br> Enter Bitcoin mining: instead of simply letting participants vote, the idea is to attach a financial cost to the vote. Anyone who wants to participate in the vote <b>(miner)</b> needs to prove that they performed some “work” – hence the term “Proof-of-Work”. This work consists of finding the solution to a cryptographic puzzle, which in simple terms can be thought of as guessing a random number. The only way of finding the random number <b>(nonce)</b> is to brute force all possible configurations: this way, the work cannot be faked but is trivial to verify by other network participants. <br><br> Miners are in constant competition between themselves: whoever finds the solution to the puzzle first obtains the right to add his block to the global ledger and gets rewarded for his efforts with newly minted bitcoin."
                    },
                    {
                        "title": "Why does Bitcoin consume energy?",
                        "text": "Solving the PoW requires substantial computing power depending on the difficulty level: the more miners join the race, the more difficult the puzzle becomes. Rather than guessing numbers manually, miners operate specialised mining equipment (ASIC) that has been specifically designed to be very good at only one single task: solving the PoW. <br><br> While newer ASIC models are substantially more energy-efficient than previous generations, they still consume a significant amount of electricity. Rising bitcoin prices make mining more attractive, as the potential reward. <br><br> The more machines a miner runs, the more likely he will find the solution to the puzzle. However, more machines also means more electricity is required to run and cool the equipment, which in turn results in higher costs for the miner."
                    },
                    {
                        "title": "How much energy does Bitcoin consume?",
                        "text": "<ul><li>It is difficult to assess how much Bitcoin mining truly consumes for multiple reasons. First, efficiency varies across mining equipment, and as we do not know the distribution of the equipment hashers use, we cannot establish with certainty how much electricity they consumed.</li><li>Second, energy is not solely required to run the machines, but also to cool them down to prevent them from overheating. Therefore, setting up a hashing facility in a region with a cold climate would offer significant advantages in terms of cool energy and cost savings. As we do not know the exact geographic location of hashing facilities, it is difficult to assess with accuracy the level of energy consumption.</li><li>	The best option available is thus to provide estimates based on certain assumptions.</li></ul>"
                    },
                    {
                        "title": "Does this mean Bitcoin boils the oceans?",
                        "text": "<ul><li>No: need to also look at the energy mix, i.e. where the energy is coming from.</li><li>Difficult to get reliable numbers, but estimates range from 20% to more than 70% (find links) of renewables.</li><li>Confirmed by our research: miners are increasingly relocating to remote regions where there is an abundance of cheap electricity (mostly hydro-powered) that remains otherwise unused as it can’t be stored for prolonged time periods.</li></ul>"
                    }
                ]
            }
        }
    }
</script>
