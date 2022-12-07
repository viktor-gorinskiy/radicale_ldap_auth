from distutils.core import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
      name="radicale_ldap_auth",
      packages=["radicale_ldap_auth"],
      version="0.0.1",
      author="Viktor Gorinskiy",
      author_email="viktor@gorinskiy.ru",
      description="Плагин авторизации в radicale под доменными пользователями",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/ericjaychi/sample-pypi-package",
      )