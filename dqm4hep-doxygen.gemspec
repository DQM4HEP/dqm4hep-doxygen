# encoding: utf-8

Gem::Specification.new do |s|
  s.name          = "dqm4hep-doxygen"
  s.version       = "0.1.0"
  s.license       = "GPL3"
  s.authors       = ["Remi Ete", "GitHub, Inc."]
  s.email         = ["opensource+dqm4hep@github.com"]
  s.homepage      = "https://github.com/dqm4hep/dqm4hep-doxygen"
  s.summary       = "DQM4hep doxygen build hosted on Github Pages"

  s.files         = `git ls-files -z`.split("\x0").select do |f|
    f.match(%r{^((_includes|_layouts|_sass|assets)/|(LICENSE|README)((\.(txt|md|markdown)|$)))}i)
  end

  s.platform      = Gem::Platform::RUBY
  s.add_runtime_dependency "jekyll", "~> 3.5"
  s.add_runtime_dependency "jekyll-seo-tag", "~> 2.0"
end
