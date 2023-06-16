<template>
  <table>
    <thead>
      <tr>
        <th v-for="(column, index) in tableColumns" :key="index">{{ column }}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(rowData, rowIndex) in transposedData" :key="rowIndex">
        <td v-for="(cellData, cellIndex) in rowData" :key="cellIndex">{{ cellData }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      tableData: [],
      tableColumns: []
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios.get('https://traderapi.tw.cpolar.io/data')
        .then(response => {
          // 將資料行列互換
          this.tableColumns = Object.keys(response.data);
          console.log(response.data)
          console.log("type is: ",typeof(response.data))
          console.log(this.tableColumns)
          console.log(this.tableColumns[0])
          console.log(this.tableColumns[1])
          console.log(this.tableColumns[2])
          console.log("-- END read columnList")
          const rowKeys = Object.keys(response.data[this.tableColumns[0]]);
          console.log("rowKeys: ",rowKeys)
          console.log(this.tableColumns[0])
          console.log("--> ",response.data['上市日'])
          this.tableData = rowKeys.map(rowKey => {
            return this.tableColumns.reduce((rowData, column) => {
              rowData[column] = response.data[column][rowKey];
              return rowData;
            }, {});
          });
        })
        .catch(error => {
          console.error('Error:', error);
        });
    }
  },
  computed: {
    transposedData() {
      // 行列互換後的資料
      return this.tableData.map(row => Object.values(row)) || [];
    }
  }
};
</script>

