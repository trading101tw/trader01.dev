<template>
  <h1>staic tabkeData</h1>
  <table>
    <thead>
      <tr>
        <th>上市日</th>
        <th>市場別</th>
        <th>產業別</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="index in tableLength" :key="index">
        <td>{{ tableData['上市日'][index - 1] }}</td>
        <td>{{ tableData['市場別'][index - 1] }}</td>
        <td>{{ tableData['產業別'][index - 1] }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  data() {
    return {
      tableData: {
        上市日: {
          0: '1962/02/09',
          1: '1962/06/08',
          2: '1969/11/14',
          3: '1971/02/01',
          4: '1990/06/06',
          5: '1991/12/05',
          6: '1994/10/22',
          7: '1962/02/09',
          8: '1964/08/24',
          9: '1978/05/20'
        },
        市場別: {
          0: '上市',
          1: '上市',
          2: '上市',
          3: '上市',
          4: '上市',
          5: '上市',
          6: '上市',
          7: '上市',
          8: '上市',
          9: '上市'
        },
        產業別: {
          0: '水泥工業',
          1: '水泥工業',
          2: '水泥工業',
          3: '水泥工業',
          4: '水泥工業',
          5: '水泥工業',
          6: '水泥工業',
          7: '食品工業',
          8: '食品工業',
          9: '食品工業'
        }
      }
    };
  },
  computed: {
    tableLength() {
      const firstColumn = this.tableData['上市日'];
      return Object.keys(firstColumn).length;
    }
  }
};
</script>

