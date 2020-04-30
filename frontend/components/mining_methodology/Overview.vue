<template>
    <v-flex xs12 md10 my-3 py-3>
        <h3 class="display-2 text-md-left">Calculating Average Country and Provincial Hashrate Share</h3>
        <v-flex class="main-text" my-3>
            <p>The mining map uses aggregate geo-location data based on the IP addresses of hashers connecting to mining pools.</p>
            <v-flex class="assumption" mb-4 pa-3>
                <span><u>Assumption 1</u>: geo-location data of hashers collected by mining pools provides an accurate picture of global hashrate location. </span>
            </v-flex>
            <p>Aggregate data contributed by participating mining pools represents approximately 37% of Bitcoin’s total hashrate for the period from April 2019 to April 2020. We use this data as a proxy for the geographic distribution of Bitcoin’s total hashrate, assuming that it is representative of the total hashrate distribution (please see the next section for a discussion of the limitations of this approach).</p>
            <v-flex class="assumption" mb-4 pa-3>
                <span><u>Assumption 2</u>: data provided by participating mining pools constitutes a representative sample of Bitcoin’s total geographic hashrate distribution. </span>
            </v-flex>
            <p>Participating mining pools provide the average monthly geographic distribution of their respective hashrate. This data is then aggregated by CCAF and used to extrapolate the global hashrate distribution. </p>
            <p>With the exception of China, hashrate data is currently only available at the country level. We hope that we can add further granularity in the future to better represent regions with significant hashing activities (e.g. Siberia in Russia, Washington and New York States in the US, or Québec and Alberta in Canada).</p>

            <!--            <v-data-table-->
<!--                    :headers="headers"-->
<!--                    :items="items"-->
<!--                    item-key="name"-->
<!--                    hide-actions-->
<!--            >-->
<!--                <template v-slot:items="props">-->
<!--                    <tr>-->
<!--                        <td>{{ props.item.parameter }}</td>-->
<!--                        <td>{{ props.item.description }}</td>-->
<!--                        <td>{{ props.item.unit }}</td>-->
<!--                        <td>{{ props.item.source }}</td>-->
<!--                    </tr>-->
<!--                </template>-->
<!--            </v-data-table>-->
        </v-flex>
        <h3 class="display-2 text-md-left">Limitations</h3>
        <v-flex class="main-text" my-3>
            <p>Every model has its limitations resulting from the application of specific assumptions. There are two particular limitations arising from the approach described above.</p>
        </v-flex>
        <h3 class="display-2 text-md-left">Usage of VPNs or proxy services by miners</h3>
        <v-flex class="main-text" my-3>
            <p>It is no secret in the industry that hashers in certain locations use virtual private networks (VPNs) or proxy services to hide their IP address and thus location. Such behaviour can distort the overall geographic distribution and result in an overestimation of hashrate in some provinces or countries. This effect is particularly visible in the Chinese province of Zhejiang. To mitigate this effect, the research team has divided the hashrate of Zhejiang province proportionally among its neighboring provinces. This approach seems reasonable given that hashers tend to select the nearest VPN server to their location in order to lower latency and submit shares more quickly to the pool.</p>
        </v-flex>
        <h3 class="display-2 text-md-left">Sample may not be representative</h3>
        <v-flex class="main-text" my-3>
            <p>The Bitcoin mining map is based on an extrapolation of a sample of mining pool data. This sample may not be fully representative for the following two reasons: first, it represents only a little more than a third of the total hashrate; and second, the data is provided by three Bitcoin mining pools that are all headquartered in China. </p>
            <p>There are reasons to believe that the sample nevertheless represents an accurate picture of the actual hashrate distribution. For one, all participating pools maintain servers in various geographies across the globe to serve their foreign customer base with minimal latency. Furthermore, Chinese pools have dominated Bitcoin mining in recent years, among others because of their relatively low fee structure which has attracted numerous non-Chinese hashers. </p>
            <p>The research team is actively looking to partner with additional mining pools and hashers to improve the accuracy and reliability of the mining map. Please do not hesitate to
                <nuxt-link to="/contact">
                    get in touch
                </nuxt-link>
                if you would like to contribute. </p>
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
