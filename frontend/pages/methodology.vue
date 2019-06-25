<template>
    <v-layout id="wrap-container2" justify-center align-center wrap my-4>
        <div style="border: 4px solid red;">
        <h3 style="text-align: center;">This is a sample page. To review the methodology section, please, follow this link <a href="http://review.cbeci.org">review.cbeci.org</a></h3>
        </div>
        <v-flex xs10>
            <v-layout mb-4 justify-center align-center>
                <h1 class="display-2">Methodology</h1>
            </v-layout>
            <h3 class="headline font-weight-bold">What is the CBECI?</h3>
            <v-flex class="main-text" my-3>
                <p>The CBECI is an index that attempts to estimate the total energy consumption of the Bitcoin network. It is an adaptation of an approach initially suggested by <a href="http://blog.zorinaq.com/bitcoin-electricity-consumption/" target="_blank">Marc Bevand</a>.</p>
                <p>The CBECI calculates a range limited by a lower-bound (absolute minimum energy expenditure) and an upper-bound estimate (realistic maximum energy expenditure).</p>
                <span>Parameters taken into account:</span>
                <ul>
                    <li>Hashrate</li>
                    <li>Difficulty level</li>
                    <li>Block rewards in $ (subsidy + tx fees)</li>
                    <li>Different mining equipment types</li>
                    <li>Electricity cost [adjustable]</li>
                    <li>Datacentre efficiency: PUE [adjustable]</li>
                    <li>Mining equipment efficiency (Joules per Gigahash)</li>
                </ul>
            </v-flex>
            <h3 class="headline font-weight-bold">Mining equipment efficiency</h3>
            <v-flex class="main-text" my-3>
                <p>CBECI covers the period from Oct 2014 – when ASICs became popular and displaced CPUs and FPGAs. If the 1000 W device solves 10’000 Gh per second, its efficiency is 0.1 J/Gh (Joules per Gigahash). The mining equipment efficiency over time is given below:</p>
            </v-flex>
            <v-layout my-4 justify-center align-center>
                <chart2/>
            </v-layout>
            <h3 class="headline font-weight-bold">Calculating the profitability threshold</h3>
            <v-flex class="main-text" my-3>
                <p>The underlying idea of the CBECI model is that miners will run the equipment as long as it is still profitable taking into account solely electricity costs, not taking into account cooling costs or CapEx or maintenance fees.</p>
                <v-layout justify-center align-center my-3>
                    <v-flex xs12 md9>
                        <img src="~static/images/methodology-functions/fun1.png" object-fit="contain" width="100%">
                    </v-flex>
                </v-layout>
                <p>Profitability threshold calculated as follows:</p>
                <v-layout justify-center align-center my-3>
                    <v-flex xs3 md1>
                        <img src="~static/images/methodology-functions/fun2.png" object-fit="contain" width="100%">
                    </v-flex>
                </v-layout>
                <p>For Pel = 0.05 USD/kWh, the profitability threshold over time is as follows:</p>
            </v-flex>
            <v-layout my-4 justify-center align-center>
                <chart3/>
            </v-layout>
            <v-flex class="main-text" my-3>
                <p>At any given moment for any given price exists a list of profitable equipment:</p>
                <v-layout justify-center align-center>
                    <v-flex xs12 md3>
                        <img src="~static/images/methodology-functions/fun3.png" object-fit="contain" width="100%">
                    </v-flex>
                </v-layout>
            </v-flex>
            <h3 class="headline font-weight-bold">Constructing the lower-bound estimate</h3>
            <v-flex class="main-text" my-3>
                <p>The lower-bound estimate is easy to calculate – it derives from the <b>Assumption 1</b>: all miners run the most efficient hardware available at each time period:</p>
                <v-layout justify-center align-center>
                    <v-flex xs12 md4>
                        <img src="~static/images/methodology-functions/fun4.png" object-fit="contain" width="100%">
                    </v-flex>
                </v-layout>
                <p>Pmin is power. The figures demonstrated on the website are electricity consumption per year adjusted to take account of power usage effectiveness by data centre:</p>
                <v-layout justify-center align-center>
                    <v-flex xs12 md6>
                        <img src="~static/images/methodology-functions/fun5.png" object-fit="contain" width="100%">
                    </v-flex>
                </v-layout>
            </v-flex>
            <h3 class="headline font-weight-bold">Constructing the upper-bound estimate</h3>
            <v-flex class="main-text" my-3>
                <p><b>Assumption 2</b>: all miners use the least efficient hardware available at that time period as long as that equipment is still profitable taking into account solely electricity costs.</p>
                <v-layout justify-center align-center>
                    <v-flex xs12 md5>
                        <img src="~static/images/methodology-functions/fun6.png" object-fit="contain" width="100%">
                    </v-flex>
                </v-layout>
            </v-flex>
            <h3 class="headline font-weight-bold">Constructing our “best guess”</h3>
            <v-flex class="main-text" my-3>
                <p>Best guess: an estimate within the lower and upper bound range that is most realistic:</p>
                <v-layout justify-center align-center>
                    <v-flex xs12 md4>
                        <img src="~static/images/methodology-functions/fun7.png" object-fit="contain" width="100%">
                    </v-flex>
                </v-layout>
            </v-flex>
            <h3 class="headline font-weight-bold">Unprofitable mining</h3>
            <v-flex class="main-text" my-3>
                <p>During unprofitable periods, the CBECI model returns the last known “profitable” figure assuming that the miners (who stay online) are not changing their equipment.</p>
            </v-flex>
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
