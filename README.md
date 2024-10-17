Odoo Server Error

RPC_ERROR
Odoo Server Error

Occured on desktop-ba21hmf:8070 on model ir.module.module and id 29 on 2024-10-17 15:30:47 GMT

Traceback (most recent call last):
  File "C:\18\odoo\odoo\http.py", line 1954, in _transactioning
    return service_model.retrying(func, env=self.env)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\18\odoo\odoo\service\model.py", line 137, in retrying
    result = func()
             ^^^^^^
  File "C:\18\odoo\odoo\http.py", line 1921, in _serve_ir_http
    response = self.dispatcher.dispatch(rule.endpoint, args)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\18\odoo\odoo\http.py", line 2168, in dispatch
    result = self.request.registry['ir.http']._dispatch(endpoint)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\18\odoo\odoo\addons\base\models\ir_http.py", line 330, in _dispatch
    result = endpoint(**request.params)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\18\odoo\odoo\http.py", line 728, in route_wrapper
    result = endpoint(self, *args, **params_ok)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\18\odoo\addons\web\controllers\dataset.py", line 40, in call_button
    action = call_kw(request.env[model], method, args, kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\18\odoo\odoo\api.py", line 517, in call_kw
    result = getattr(recs, name)(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\hasan\AppData\Local\Programs\Python\Python312\Lib\site-packages\decorator.py", line 232, in fun
    return caller(func, *(extras + args), **kw)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\18\odoo\odoo\addons\base\models\ir_module.py", line 75, in check_and_log
    return method(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\18\odoo\odoo\addons\base\models\ir_module.py", line 477, in button_immediate_install
    return self._button_immediate_function(self.env.registry[self._name].button_install)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\18\odoo\odoo\addons\base\models\ir_module.py", line 601, in _button_immediate_function
    registry = modules.registry.Registry.new(self._cr.dbname, update_module=True)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\hasan\AppData\Local\Programs\Python\Python312\Lib\site-packages\decorator.py", line 232, in fun
    return caller(func, *(extras + args), **kw)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\18\odoo\odoo\tools\func.py", line 97, in locked
    return func(inst, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\18\odoo\odoo\modules\registry.py", line 131, in new
    odoo.modules.load_modules(registry, force_demo, status, update_module)
  File "C:\18\odoo\odoo\modules\loading.py", line 479, in load_modules
    processed_modules += load_marked_modules(env, graph,
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\18\odoo\odoo\modules\loading.py", line 363, in load_marked_modules
    loaded, processed = load_module_graph(
                        ^^^^^^^^^^^^^^^^^^
  File "C:\18\odoo\odoo\modules\loading.py", line 226, in load_module_graph
    load_data(env, idref, mode, kind='data', package=package)
  File "C:\18\odoo\odoo\modules\loading.py", line 70, in load_data
    tools.convert_file(env, package.name, filename, idref, mode, noupdate, kind)
  File "C:\18\odoo\odoo\tools\convert.py", line 604, in convert_file
    convert_csv_import(env, module, pathname, fp.read(), idref, mode, noupdate)
  File "C:\18\odoo\odoo\tools\convert.py", line 650, in convert_csv_import
    raise Exception(env._(
Exception: Module loading medical_announcement failed: file medical_announcement\security/ir.model.access.csv could not be processed:
No matching record found for external id 'group_techcare_specialist' in field 'Group'
No matching record found for external id 'group_techcare_patient' in field 'Group'
No matching record found for external id 'group_techcare_specialist' in field 'Group'

The above server error caused the following client error:
RPC_ERROR: Odoo Server Error
    RPC_ERROR
        at makeErrorFromResponse (http://desktop-ba21hmf:8070/web/assets/086e154/web.assets_web.min.js:3058:163)
        at XMLHttpRequest.<anonymous> (http://desktop-ba21hmf:8070/web/assets/086e154/web.assets_web.min.js:3063:13)
