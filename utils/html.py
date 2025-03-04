def generate_html(data_dict):
    """
    Generates an HTML file displaying summarized statistical data of parallelepipeds.

    Parameters:
    data_dict (dict): A dictionary containing statistical data with the following keys:
        - 'avg_diag': Average main diagonal
        - 'avg_volume': Average volume
        - 'avg_surface_area': Average surface area
        - 'avg_alpha': Average alpha angle
        - 'avg_beta': Average beta angle
        - 'avg_gamma': Average gamma angle
        - 'avg_radius_described_sphere': Average radius of the circumscribed sphere
        - 'avg_volume_described_sphere': Average volume of the circumscribed sphere

    Returns:
    None: Writes the generated HTML content to 'outputs/data_summary.html'.
    """

    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Summary</title>
    <style>
        body {{
            background-color: #000000;
            color: #FFFFFF;
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }}
        .container {{
            text-align: center;
            width: 80%;
            margin: 0 auto;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
            background-color: #1c1c1c;
        }}
        th, td {{
            border: 1px solid #444;
            padding: 10px;
            text-align: center;
        }}
        th {{
            background-color: #333;
        }}
        td {{
            background-color: #222;
        }}
        h1, p {{
            margin: 10px;
        }}
        .header {{
            color: #FFD700;
        }}
        #asciiArt {{
            font-family: monospace;
            white-space: pre;
            color: #FFD700;
            position: absolute;
            top: 10px;
            right: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1 class="header">Data Summary</h1>
        <p>Мы обработали полученные фигуры и подвели статистику</p>
        <table>
            <tr>
                <th>Parameter</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>Average Diagonal</td>
                <td>{data_dict['avg_diag']}</td>
            </tr>
            <tr>
                <td>Average Volume</td>
                <td>{data_dict['avg_volume']}</td>
            </tr>
            <tr>
                <td>Average Surface Area</td>
                <td>{data_dict['avg_surface_area']}</td>
            </tr>
            <tr>
                <td>Average Alpha</td>
                <td>{data_dict['avg_alpha']}</td>
            </tr>
            <tr>
                <td>Average Beta</td>
                <td>{data_dict['avg_beta']}</td>
            </tr>
            <tr>
                <td>Average Gamma</td>
                <td>{data_dict['avg_gamma']}</td>
            </tr>
            <tr>
                <td>Average Radius of Described Sphere</td>
                <td>{data_dict['avg_radius_described_sphere']}</td>
            </tr>
            <tr>
                <td>Average Volume of Described Sphere</td>
                <td>{data_dict['avg_volume_described_sphere']}</td>
            </tr>
        </table>
    </div>
    <div id="asciiArt"></div>
    <script>
        const asciiArt = [
            'MY FIRST SKRIPT\\n\\n',
            '    *********',
            '   *       **',
            '  *       * *',
            ' *********  *',
            ' *       *  *',
            ' *       *  *',
            ' *       * *',
            ' *********',
            '\\n\\nI LOVE PYTHON'
        ];
        let artIndex = 0;
        function displayArt() {{
            if (artIndex < asciiArt.length) {{
                document.getElementById('asciiArt').innerText += asciiArt[artIndex] + '\\n';
                artIndex++;
                setTimeout(displayArt, 400);
            }}
        }}
        displayArt();
    </script>
</body>
</html>
    """

    with open("outputs/data_summary.html", "w") as file:
        file.write(html_content)
