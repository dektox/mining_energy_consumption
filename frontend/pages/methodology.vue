<template>
    <v-layout id="wrap-container2" column justify-center align-center>
        <v-flex my-3>
          <span style="font-size: 32px">
            Methodology
          </span>
        </v-flex>
        <v-flex xs12 md10 my-3 class="card-text">
            <p><b> What is the CBECI?</b></p>
            <span>
                The CBECI is an index that attempts to estimate the total energy consumption of the Bitcoin network. It is an adaptation of an approach initially suggested by <a href="http://blog.zorinaq.com/bitcoin-electricity-consumption/" target="_blank">Marc Bevand</a>.
            </span><br>
            <span>
                The CBECI calculates a range limited by a lower-bound (absolute minimum energy expenditure) and an upper-bound estimate (realistic maximum energy expenditure).
            </span><br>
            <span>
                Parameters taken into account:
            </span><br>
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
                    Electricity cost [adjustable]
                </li>
                <li>
                    Datacentre efficiency: PUE [adjustable]
                </li>
                <li>
                    Mining equipment efficiency (Joules per Gigahash)
                </li>
            </ul><br>
            <p><b>Mining equipment efficiency</b></p>
            <span>
                CBECI covers the period from Oct 2014 – when ASICs became popular and displaced CPUs and FPGAs. If the 1000 W device solves 10’000 Gh per second, its efficiency is 0.1 J/Gh (Joules per Gigahash). The mining equipment efficiency over time is given below:
            </span><br><br>
            <v-layout column justify-center align-center>
                <chart2/>
            </v-layout><br>
            <p><b>Calculating the profitability threshold</b></p>
            <span>
                The underlying idea of the CBECI model is that miners will run the equipment as long as it is still profitable taking into account solely electricity costs, not taking into account cooling costs or CapEx or maintenance fees.
            </span><br><br>
            <v-layout justify-center align-center>
                <v-flex xs12 md9>
                    <img src="~static/fun1.png" object-fit="contain" width="100%">
                </v-flex>
            </v-layout><br>
            <span>
                Profitability threshold calculated as follows:
            </span><br><br>
            <v-layout justify-center align-center>
                <v-flex xs3 md1>
                    <img src="~static/fun2.png" object-fit="contain" width="100%">
                </v-flex>
            </v-layout><br>
            <span>
                For Pel = 0.05 USD/kWh, the profitability threshold over time is as follows:
            </span><br><br>
            <v-layout column justify-center align-center>
                <chart3/>
            </v-layout><br>
            <span>
                At any given moment for any given price exists a list of profitable equipment:
            </span><br><br>
            <v-layout justify-center align-center>
                <v-flex xs12 md3>
                    <img src="~static/fun3.png" object-fit="contain" width="100%">
                </v-flex>
            </v-layout><br>
            <p><b>Constructing the lower-bound estimate</b></p>
            <span>
                The lower-bound estimate is easy to calculate – it derives from the <b>Assumption 1</b>: all miners run the most efficient hardware available at each time period:
            </span><br><br>
            <v-layout justify-center align-center>
                <v-flex xs12 md4>
                    <img src="~static/fun4.png" object-fit="contain" width="100%">
                </v-flex>
            </v-layout><br>
            <span>
                Pmin is power. The figures demonstrated on the website are electricity consumption per year adjusted to take account of power usage effectiveness by data centre:
            </span><br><br>
            <v-layout justify-center align-center>
                <v-flex xs12 md6>
                    <img src="~static/fun5.png" object-fit="contain" width="100%">
                </v-flex>
            </v-layout><br>
            <p><b>Constructing the upper-bound estimate</b></p>
            <span>
                <b>Assumption 2</b>: all miners use the least efficient hardware available at that time period as long as that equipment is still profitable taking into account solely electricity costs.
            </span><br><br>
            <v-layout justify-center align-center>
                <v-flex xs12 md5>
                    <img src="~static/fun6.png" object-fit="contain" width="100%">
                </v-flex>
            </v-layout><br>
            <p><b>Constructing our “best guess”</b></p>
            <span>
                Best guess: an estimate within the lower and upper bound range that is most realistic:
            </span><br><br>
            <v-layout justify-center align-center>
                <v-flex xs12 md4>
                    <img src="~static/fun7.png" object-fit="contain" width="100%">
                </v-flex>
            </v-layout><br>
            <p><b>Unprofitable mining</b></p>
            <span>
                During unprofitable periods, the CBECI model returns the last known “profitable” figure assuming that the miners (who stay online) are not changing their equipment.
            </span><br>
        </v-flex>
    </v-layout>
</template>

<script>
import Chart2 from '~/components/Chart2'
import Chart3 from '~/components/Chart3'

export default {
    name: 'methodology',
    components: {
        chart2: Chart2,
        chart3: Chart3
    },
    data() {
        return {
        }
    }
}
</script>
