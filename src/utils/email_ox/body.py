from .webscraper.cepea import ox_table
from pynliner import Pynliner

css = """\
      * {
          font-family: Arial, Helvetica, sans-serif;
      }

      #fat_ox {
          padding-left: 7%;
          width: 35%;
          height: 45%;
      }

      #ox_table {
          border-collapse: collapse;
          width: 50%;
      }

      #ox_table td, #ox_table th {
          border: 1px solid #ddd;
          padding: 7px;
      }
      #ox_table th {
        text-align: left;
        background-color: #4CAF50;
        color: white;
      }
    """

html = """\
<html>
  <head>
    <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
    <meta content="utf-8" http-equiv="encoding">
  </head>
  <body>
    <img id="globo_rural" src="http://3.bp.blogspot.com/-XPALlNX7vis/UjT9CI-j8SI/AAAAAAAAADs/CtyTDmMYj00/s640/20100817112517-globo_rural.jpg" alt="Globo Rural.jpg" >
    <p>
      Saudações, segue a cotação mais atual do arroba do boi gordo. 
      <h3>Boi Gordo</h3>
      Arroba (15kg) - à vista<br>
      <br>
      <div id="table_img">
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
        <br>
        Fonte: CEPEA
        </p>
        <br>
        <br>
        <img id="fat_ox" src="https://blogs.canalrural.com.br/blogdoscot/wp-content/uploads/sites/7/2018/11/181114_Imagem_Carta_Boi_2_nm.jpg" alt="Boi Gordo.jpg"  >
      </div>
  </body>
</html>
""".format(data=ox_table[0], valor_rs=ox_table[1], var_dia=ox_table[2], var_mes=ox_table[3], valor_us=ox_table[4])

p = Pynliner()

#Put the css string into html string
body =  p.from_string(html).with_cssString(css).run()