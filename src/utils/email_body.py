from webscraper.cepea import ox_table

body = """\
<html>
  <head>
    <link rel= "stylesheet" type= "text/css" href= "./table_style.css">
  </head>
  <body>
    <img src="http://3.bp.blogspot.com/-XPALlNX7vis/UjT9CI-j8SI/AAAAAAAAADs/CtyTDmMYj00/s640/20100817112517-globo_rural.jpg" alt="Globo Rural.jpg" >
    <p>
      <br>
      <h3>Boi</h3>
      Arroba (15kg) - à vista<br>
      <br>
      <table id="ox_table">
        <tr>
          <th>Data</th>
          <th>Valor R$</th>
          <th>Var. /Dia</th>
          <th>Var. /Mês</th>
          <th>Valor US$</th>
        </tr>
        <tr>
          <td>{data}</td>
          <td>{valor_rs}</td>
          <td>{var_dia}</td>
          <td>{var_mes}</td>
          <td>{valor_us}</td>
        </tr>
      </table>
    </p>
    <br>
    <br>
    <img src="https://blogs.canalrural.com.br/blogdoscot/wp-content/uploads/sites/7/2018/11/181114_Imagem_Carta_Boi_2_nm.jpg" alt="Boi Gordo.jpg" style="width: 35%;heigth: 35%" >
  </body>
</html>
""".format(data=ox_table[0], valor_rs=ox_table[1], var_dia=ox_table[2], var_mes=ox_table[3], valor_us=ox_table[4])

f = open('./html/email_body.html','w')

f.write(body)
f.close()