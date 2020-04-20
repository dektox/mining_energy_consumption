<template>
    <v-flex xs12 md10 my-3 py-3>
        <h3 class="display-2 text-md-left">Calculating Average Country and Provincial Hashrate Share</h3>
        <v-flex class="main-text" my-3>
            <p>All together, data contributed by participating pools amounts to approximately 35% of Bitcoin’s total hashrate. To build this mining map, the research team assumes that the geographic distribution of participating pools’ hashrate is representative of the geographic distribution of Bitcoin’s total hashrate.</p>
            <p>Variables collected from mining pools are described in the Table below. </p>
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
        <h3 class="display-2 text-md-left">Limitations</h3>
        <v-flex class="main-text" my-3>
            <p>There are two major limitations in the above calculations that readers should be aware of.</p>
        </v-flex>
        <h3 class="display-2 text-md-left">Usage of VPNs or proxy services by miners</h3>
        <v-flex class="main-text" my-3>
            <p>It is commonly known in the industry that miners in certain regions use VPNs or proxy services to hide their IP address and apparent location. This VPN distortion effect results in an overestimate of hashrate in some regions, particularly in Zhejiang, China. To mitigate this effect, the research team divided the hashrate of Zhejiang province equally among its neighboring provinces: though miners use VPN to change their IP address, they still require a fast and stable connection to send their hashpower to the pool; as a result, miners tend to select the nearest VPN server to lower the latency.</p>
        </v-flex>
        <h3 class="display-2 text-md-left">Extrapolating geographic distribution of Bitcoin’s total hashrate</h3>
        <v-flex class="main-text" my-3>
            <p>As discussed above, the Bitcoin mining map is based on data provided by three Bitcoin mining pools that represent 35% of Bitcoin’s total hashrate. While extrapolating Bitcoin’s hashrate geographic distribution might be seen as a shortcut, it is nevertheless the most accurate representation of Bitcoin’s hashrate distribution around the world. It is the CCAF’s hope that this first version of the map will incentivise other Bitcoin mining pools to contribute to this research project.</p>
        </v-flex>
    </v-flex>
</template>

<script>
export default {
    name: 'Overview2',
    data() {
        return {
            headers: [
                { text: 'Variable name', sortable: false, value: 'parameter'},
                { text: 'Description', sortable: false, value: 'description'},
                { text: 'Unit', sortable: false, value: 'unit'}
            ],
            items: [
                {
                    parameter: 'Date',
                    description: 'Month and year of the corresponding period',
                    unit: 'NA',
                },
                {
                    parameter: 'Country',
                    description: 'Country name from which hashrate originates',
                    unit: 'NA',
                },
                {
                    parameter: 'Province (China only)',
                    description: 'Province name from which hashrate originates',
                    unit: 'NA',
                },
                {
                    parameter: 'Monthly hashrate per province/country',
                    description: 'The number of hashes per second performed in the corresponding province/country in the last 30 days',
                    unit: 'Ph/s or Th/s',
                }
            ]
        }
    }
}
</script>
