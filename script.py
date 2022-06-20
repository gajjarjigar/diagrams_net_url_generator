import urllib.parse
import zlib
import base64

def decode_base64_and_inflate( b64string ):
    decoded_data = base64.b64decode( b64string )
    return zlib.decompress( decoded_data , -15)

def deflate_and_base64_encode( string_val ):
    zlibbed_str = zlib.compress( string_val )
    compressed_string = zlibbed_str[2:-4]
    return base64.b64encode( compressed_string )


original_xml = '<mxGraphModel dx="1426" dy="708" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0"><root><mxCell id="0" /><mxCell id="1" parent="0" /><mxCell id="o13WNn51d6DNZ1hpwu64-1" value="&lt;div&gt;Hello World&lt;/div&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1"><mxGeometry x="190" y="280" width="290" height="20" as="geometry" /></mxCell></root></mxGraphModel>'

safe_string = urllib.parse.quote(original_xml.strip(), safe='')
graph_data = deflate_and_base64_encode(safe_string.encode()).decode()
mxfile = f'<mxfile host="app.diagrams.net" modified="2022-06-20T12:03:56.006Z" agent="5.0 (Macintosh)" version="15.3.0" type="device"><diagram name="Page-1">{graph_data}</diagram></mxfile>'
p = urllib.parse.quote(mxfile, safe='')
url = f'https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#R{p}'
print(url)
