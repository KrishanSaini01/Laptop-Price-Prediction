from flask import Flask, render_template, url_for, request
import joblib
import pandas as pd

app = Flask(__name__)


model = joblib.load(r"Model\\RandomForestRegressor.lb")


df = pd.read_csv(r"Data\\laptop_price.csv", encoding='latin1')

Company_list = df['Company'].unique().tolist()
Company_dict = {c: i + 1 for i, c in enumerate(Company_list)}

Product_list = df['Product'].unique().tolist()
Product_dict = {p: i + 1 for i, p in enumerate(Product_list)}

TypeName_dict = {
    'Ultrabook': 1, 'Notebook': 2, 'Netbook': 3,
    'Gaming': 4, '2 in 1 Convertible': 5, 'Workstation': 6
}

ScreenResolution_list = df['ScreenResolution'].unique().tolist()
ScreenResolution_dict = {s: i + 1 for i, s in enumerate(ScreenResolution_list)}

Cpu_list = df['Cpu'].unique().tolist()
Cpu_dict = {c: i + 1 for i, c in enumerate(Cpu_list)}

Ram_list = sorted(df['Ram'].unique().tolist(), key=lambda x: int(x.replace('GB', '')))

Memory_list = df['Memory'].unique().tolist()
Memory_dict = {m: i + 1 for i, m in enumerate(Memory_list)}

Gpu_list = df['Gpu'].unique().tolist()
Gpu_dict = {g: i + 1 for i, g in enumerate(Gpu_list)}

OpSys_list = df['OpSys'].unique().tolist()
OpSys_dict = {o: i + 1 for i, o in enumerate(OpSys_list)}


def get_dropdown_options():

    return {
        'companies': Company_list,
        'products': Product_list,        
        'typenames': list(TypeName_dict.keys()),
        'screenresolutions': ScreenResolution_list,
        'cpus': Cpu_list,
        'rams': Ram_list,
        'memories': Memory_list,
        'gpus': Gpu_list,
        'opsys_options': OpSys_list,
    }


@app.route('/')
def index():
    return render_template('index.html', **get_dropdown_options())


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/project')
def project():
    return render_template('project.html', **get_dropdown_options())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    company = request.form['company']
    product = request.form['product']
    typename = request.form['typename']
    inches = float(request.form['inches'])
    screenresolution = request.form['screenresolution']
    cpu = request.form['cpu']
    ram = int(request.form['ram'].replace('GB', ''))
    memory = request.form['memory']
    gpu = request.form['gpu']          
    opsys = request.form['opsys']
    weight = float(request.form['weight'])

    company = Company_dict.get(company)
    product = Product_dict.get(product)
    typename = TypeName_dict.get(typename)
    screenresolution = ScreenResolution_dict.get(screenresolution)
    cpu = Cpu_dict.get(cpu)
    memory = Memory_dict.get(memory)
    gpu = Gpu_dict.get(gpu)
    opsys = OpSys_dict.get(opsys)

    print(company, product, typename, inches, screenresolution, cpu, ram, memory, gpu, opsys, weight)
    print(type(company), type(product), type(typename), type(inches), type(screenresolution),type(cpu), type(ram), type(memory), type(gpu), type(opsys), type(weight))

    data = [[company, product, typename, inches, screenresolution, cpu, ram, memory, gpu, opsys, weight]]
    pred = model.predict(data)
    print("Prediction 🤖🤖>>>>", pred)

    return render_template('project.html', **get_dropdown_options(), prediction=pred[0])


if __name__ == "__main__":
    app.run(debug=True)