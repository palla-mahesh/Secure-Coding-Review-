from flask import render_template
from app import app
from analyzers.static_analyzer import StaticAnalyzer

# Analysis Route
@app.route('/analyze/<filename>')
def analyze(filename):

    filepath = 'static/uploads/' + filename

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            code = file.read()

        analyzer = StaticAnalyzer()

        results = analyzer.analyze_code(code)

        return render_template(
            'results.html',
            filename=filename,
            results=results
        )

    except Exception as e:

        return f"Error analyzing file: {str(e)}"