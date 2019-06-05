<template>
    <v-layout justify-center align-left>
        <v-flex xs12 md10>
            <b>
                What is the CBECI?
            </b>
            <span>
            The CBECI is an index that attempts to estimate the total energy consumption of the Bitcoin network. It is an adaptation of an approach initially suggested by Marc Bevand.1 The CBECI calculates a range limited by a lower-bound (absolute minimum energy expenditure) and an upper-bound estimate (realistic maximum energy expenditure).
        </span>
            Parameters taken into account:
            <ul>
                <li>
                    Hashrate
                </li>
                <li>
                    Difficulty level
                </li>
                <li>
                    Block rewards in $ (subsidy + tx fees)
                </li>
                <li>
                    Different mining equipment types
                </li>
                <li>
                    Electricity cost
                </li>
                <li>
                    Datacentre efficiency: PUE
                </li>
            </ul><br>
            <b>
                Constructing the lower-bound estimate
            </b>
            <span>
            Lower-bound: easy to calculate – Assumption 1: all miners run the most efficient hardware available at each time period.
            Provide a table with the hardware used for each time period?
        </span><br>
            <b>
                Constructing the upper-bound estimate
            </b>
            <span>
            Upper-bound: a bit harder – inspired by Marc Bevand’s methodology: Assumption 2: all miners use the least efficient hardware available at that time period as long as that equipment is still profitable taking into account solely electricity costs.
        </span>
            Steps to construct the upper bound:
            <ul>
                <li>
                    Step 1: scrape hashrate, BTC price in USD, difficulty, and block reward (subsidy + transaction fee) from coinmetrics.io;
                </li>
                <li>
                    Step 2: collect all mining hardware available to hashers for each of the covered time periods, including energy efficiency parameters
                </li>
                <li>
                    Step 3: calculate the profitability of each mining hardware type:
                </li>
            </ul><br>
            <span>
            Assumption 3: price of electricity ($ per KwH – can be customised)
        </span>
            <span>
            Assumption x: geographic location of data centres → energy consumed to cool down the machines
        </span>
            <span>
            Simulate the profitability of each hardware type throughout Bitcoin’s lifecycle given the actual Hashrate
        </span>
            <span>
            Assumption 4: Whenever the least efficient hardware becomes unprofitable, miners switch to the second least efficient hardware that is still profitable in terms of electricity costs.
        </span><br>
            <b>Constructing our “best guess”</b>
            <span>
            Best guess: an estimate within the lower and upper bound range that is most realistic
        </span>
            <span>
            Explain details
        </span>
            <span>
            How does the CBECI compare to other estimates?
        </span><br>
            <b>List main estimates and briefly explain how they differ</b>
        </v-flex>
    </v-layout>
</template>

<script>

    export default {
        name: 'methodology',
        data() {
            return {
            }
        }
    }
</script>
