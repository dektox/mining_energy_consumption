<template>
    <v-layout align-center justify-center column>
        <h2 class="display-1">
            Overview
        </h2>
        <h3 class="headline font-weight-bold text-md-left">Summary</h3>
        <v-flex class="main-text" my-3>
            <p>The Cambridge Bitcoin Electricity Consumption Index (CBECI) provides a real-time estimate of the total electricity load and consumption of the Bitcoin network. The model is based on a bottom-up approach initially developed by <a href="http://blog.zorinaq.com/bitcoin-electricity-consumption/" target="_blank">Marc Bevand</a> in 2017 that takes different types of available mining hardware as the starting point.</p>
            <p>Given that the exact electricity consumption cannot be determined, the CBECI provides a range of possibilities consisting of a <b>lower bound</b> (floor) and an <b>upper bound</b> (ceiling) estimate. Within the boundaries of this range, a <b>best-guess</b> estimate is calculated to provide a more realistic figure that we believe comes closest to Bitcoin’s real annual electricity consumption.</p>
            <p>The lower bound estimate corresponds to the absolute minimum total electricity expenditure based on the best case assumption that all miners always use the most energy-efficient equipment available on the market. The upper bound estimate specifies the absolute maximum total electricity expenditure based on the worst case assumption that all miners always use the least energy-efficient hardware available on the market as long as running the equipment is still profitable in electricity terms. The best-guess estimate is based on the assumption that miners use a basket of profitable hardware rather than a single model.</p>
        </v-flex>
        <h3 class="headline font-weight-bold text-md-left">Representation</h3>
        <v-flex class="main-text" my-3>
            <p>The CBECI landing page displays two numbers for each type of estimate.</p>
            <p>The first number refers to the total <b>electrical power</b> consumed by the Bitcoin network and is expressed in gigawatts (GW). This figure is updated every 30 seconds and corresponds to the rate at which Bitcoin uses electricity.</p>
            <p>The second number refers to the total <b>yearly electricity consumption</b> of the Bitcoin network and is expressed in terawatt-hours (TWh). We annualise Bitcoin’s electricity consumption assuming continuous power usage at the aforementioned rate over the period of one year. We apply a <b>7-day moving average</b> to the resulting data point in order to make the output value less dependent of short-term hashrate movements, and thus more suitable for comparisons with alternative uses of electricity.</p>
        </v-flex>
        <h3 class="headline font-weight-bold text-md-left">Model parameters</h3>
        <v-flex class="main-text" my-3>
            <p>The model takes into account the parameters outlined in <b>Table 1</b> below. The following sections will specify how each estimate is calculated and what assumptions have been used.</p>
            <v-toolbar flat color="white">
                <v-toolbar-title>Table 1: CBECI model parameters</v-toolbar-title>
            </v-toolbar>
            <v-data-table
                    :headers="headers"
                    :items="items"
                    item-key="name"
                    hide-actions
            >
                <template v-slot:items="props">
                    <tr>
                        <td>{{ props.item.parameter }}</td>
                        <td>{{ props.item.description }}</td>
                        <td>{{ props.item.unit }}</td>
                        <td>{{ props.item.source }}</td>
                    </tr>
                </template>
            </v-data-table>
        </v-flex>
    </v-layout>
</template>

<script>
export default {
    name: 'Overview',
    data() {
        return {
            headers: [
                { text: 'Parameter', sortable: false, value: 'parameter'},
                { text: 'Description', sortable: false, value: 'description'},
                { text: 'Measure/Unit', sortable: false, value: 'unit'},
                { text: 'Source', sortable: false, value: 'source'},
            ],
            items: [
                {
                    parameter: 'Network hashrate',
                    description: 'Total number of hashes produced by miners',
                    unit: 'Exahashes per second (Eh/s)',
                    source: 'Dynamic: Blockchain.info',
                },
                {
                    parameter: 'Network hashrate',
                    description: 'Total number of hashes produced by miners',
                    unit: 'Exahashes per second (Eh/s)',
                    source: 'Dynamic: Blockchain.info',
                },
                {
                    parameter: 'Network hashrate',
                    description: 'Total number of hashes produced by miners',
                    unit: 'Exahashes per second (Eh/s)',
                    source: 'Dynamic: Blockchain.info',
                },
                {
                    parameter: 'Network hashrate',
                    description: 'Total number of hashes produced by miners',
                    unit: 'Exahashes per second (Eh/s)',
                    source: 'Dynamic: Blockchain.info',
                },
                {
                    parameter: 'Network hashrate',
                    description: 'Total number of hashes produced by miners',
                    unit: 'Exahashes per second (Eh/s)',
                    source: 'Dynamic: Blockchain.info',
                },
            ]
        }
    }
}
</script>
