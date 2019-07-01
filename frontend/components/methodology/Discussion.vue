<template>
    <v-layout align-center justify-center column>
        <h2 class="display-1">
            Discussion
        </h2>
        <h3 class="headline font-weight-bold text-md-left">Limitations of the model</h3>
        <v-flex class="main-text" my-3>
            <p>Every model is an incomplete representation of reality that relies on specific assumptions, some of which may be debatable. As a result, every model has limitations that need to be discussed. In particular, the current CBECI model exhibits the following limitations (the list is non-exhaustive):</p>
            <p>While most limitations do not have a major impact on the performance of the model, we are aware of its imperfections. The CBECI is an ongoing project that is maintained on a continuous basis. The model will be refined in response to changing circumstances, with all changes being transparently highlighted.</p>
            <p>In case you would like to provide suggestions on how we could improve the index, please feel free to send us a message using <nuxt-link to="/contact/">this form</nuxt-link>.</p>
        </v-flex>
        <h3 class="headline font-weight-bold text-md-left">How does the CBECI compare to other estimates?</h3>
        <v-flex class="main-text" my-3>
            <p>There have been multiple attempts in the past to analyse the electricity consumption of the Bitcoin network and assess its environmental footprint. A list of available studies and articles is presented in <b>Table 2</b>. With the exception of Alex De Vries <a target="_blank" href="https://digiconomist.net/bitcoin-energy-consumption">“Bitcoin Electricity Consumption Index” (BECI)</a>, there is no live index tracking Bitcoin’s electricity load and consumption in real time.</p>
            <v-toolbar flat color="white">
                <v-toolbar-title>Table 2: Overview of previous studies on Bitcoin’s electricity usage and/or carbon emissions</v-toolbar-title>
            </v-toolbar>
            <v-data-table
                    :headers="headers"
                    :items="items"
                    item-key="name"
                    hide-actions
            >
                <template v-slot:items="props">
                    <tr>
                        <td>{{ props.item.author }}</td>
                        <td>{{ props.item.date }}</td>
                        <td>{{ props.item.title }}</td>
                        <td>{{ props.item.approach }}</td>
                        <td><a target="_blank" :href="props.item.link">Link</a></td>
                    </tr>
                </template>
            </v-data-table>
        </v-flex>
        <v-flex class="main-text" my-3>
            <p>Each study is based on a set of assumptions that can be put into question. As a result, the design of each study - including our own analysis - has its own pitfalls and limitations. Some papers, however, have been criticised for applying overly simplistic assumptions and containing non-trivial errors such as inappropriate averaging over time periods or simple extrapolations. For a more thorough review of previous studies, see Koomey (2019).</p>
            <p>The CBECI has been designed with the aforementioned studies in mind. We have carefully reviewed the various methodologies and incorporated best practices. This website attempts to provide comprehensive documentation with transparent version control, highlight the model’s dependence on the electricity cost assumption by allowing visitors to adjust the default value, and openly present the uncertainties and limitations of the model. Feedback and suggestions for further improvements can be given <nuxt-link to="/contact/">here</nuxt-link>.
            </p>
        </v-flex>
    </v-layout>
</template>

<script>
export default {
    name: 'Discussion',
    data() {
        return {
            headers: [
                { text: 'Author', sortable: false, value: 'author'},
                { text: 'Date of publication', sortable: false, value: 'date'},
                { text: 'Title', sortable: false, value: 'title'},
                { text: 'Approach', sortable: false, value: 'approach'},
                { text: 'Link', sortable: false, value: 'link'},
            ],
            items: [
                {
                    author: 'Stoll, C., Klaaßen, L., and Gallersdorfer, U.',
                    date: '2019',
                    title: 'The Carbon Footprint of Bitcoin',
                    approach: 'Bottom-up',
                    link: 'https://www.cell.com/action/showPdf?pii=S2542-4351%2819%2930255-7'
                },
                {
                    author: 'Krause, M. J., and Tolaymat, T',
                    date: 'November 2018',
                    title: 'Quantification of energy and carbon costs for mining cryptocurrencies',
                    approach: 'Bottom-up',
                    link: 'https://www.nature.com/articles/s41893-018-0152-7.pdf'
                },
                {
                    author: 'Mora, C., Rollins, R.L., Taladay, K., Kantar, M.B., Chock, M.K., Shimada, M., and Franklin, E.C.',
                    date: 'October 2018',
                    title: 'Bitcoin emissions alone could push global warming above 2°C',
                    approach: 'Top-down (relies on Digiconomist’s estimate)',
                    link: 'https://www.nature.com/articles/s41558-018-0321-8.pdf'
                },
                {
                    author: 'McCook, H.',
                    date: 'August 2018',
                    title: 'The cost & sustainability of Bitcoin',
                    approach: 'Bottom-up',
                    link: 'https://www.academia.edu/37178295/The_Cost_and_Sustainability_of_Bitcoin_August_2018_'
                },
                {
                    author: 'De Vries, A.',
                    date: 'May 2018',
                    title: 'Bitcoin’s Growing Energy Problem',
                    approach: 'Top-down',
                    link: 'https://www.researchgate.net/publication/325188032_Bitcoin\'s_Growing_Energy_Problem'
                },
                {
                    author: 'Vranken, H.',
                    date: 'October 2017',
                    title: 'Sustainability of bitcoin and blockchains',
                    approach: 'Bottom-up',
                    link: 'https://www.sciencedirect.com/science/article/pii/S1877343517300015'
                },
                {
                    author: 'Bevand, M.',
                    date: 'February 2017',
                    title: 'Electricity consumption of Bitcoin: a market-based and technical analysis',
                    approach: 'Bottom-up',
                    link: 'http://blog.zorinaq.com/bitcoin-electricity-consumption/#fnref:refD:1'
                },
                {
                    author: 'Hayes, A. S.',
                    date: 'March 2015',
                    title: 'A Cost Production Model for Bitcoin',
                    approach: 'Top-down',
                    link: 'http://www.economicpolicyresearch.org/econ/2015/NSSR_WP_052015.pdf'
                },
                {
                    author: 'O’Dwyer, K.L., and Malone, D.',
                    date: 'September 2014',
                    title: '“Bitcoin Mining and its Energy Footprint',
                    approach: 'Top-down',
                    link: 'https://doi.org/10.1049/cp.2014.0699'
                },
            ]
        }
    }
}
</script>
