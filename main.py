import csv

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def pushpin_color(condition):
    if condition == "GOOD":
        return "msn_grn-pushpin"
    if condition == "REGULAR":
        return "#msn_ylw-pushpin"
    return "#msn_red-pushpin"


def csvToKml():
    fname = input("Informe o nome de arquivo SEM extensão: ")
    print(f"Converting {fname}.csv")
    data = csv.reader(open(fname + '.csv'), delimiter=',')

    #Pule a primeira linha
    data.__next__()

    #Abra o arquivo de destino
    f = open('csv2kml.kml', 'w')

    #Escrevendo o arquivo
    f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
    f.write("<kml xlmns='http://earth.google.com/kml/2.1>\n")
    f.write("<Document>\n")
    for row in data:
        print(f"adicionando linha {data.line_num} ao KML...")
        f.write("   <Placemark>\n")
        f.write("      <name>" + str(row[5]) + "</name>\n")
        f.write("      <description>")
        f.write("<![CDATA[<img style=\"max-width:500px;\" src=\"file:///C:/Users/frasia/Desktop/Vistoria F Dallegrave - Fotos/" + str(row[4]) + ".jpg\">" + str(row[0]) + " " + str(row[2]) + "]]></description>\n")
        f.write("      <styleUrl>" + pushpin_color(row[2]) + "</styleUrl>\n")
        f.write("      <Point>\n")
        f.write("         <coordinates>" + str(row[7] + "," + str(row[6]) + "," + str("0") + "</coordinates>\n"))
        f.write("      </Point>\n")
        f.write("   </Placemark>\n")
    f.write("</Document>\n")
    f.write("</kml>\n")
    print("Arquivo foi criado com sucesso!")
    print("Pressione ENTER para sair.")
    input()
    f.close()

if __name__ == '__main__':
    print_hi('Welcome to CappiKML - a custom CSV to KML conveter')
    csvToKml()

