export PYTHONPATH="$(realpath .)"
export YEAR=$1
export DAY=$2

dir="${YEAR}/${DAY}"
if [[ ! -d ${dir} ]]; then
    mkdir -p "${dir}"
fi
for n in 1 2; do
    f="${dir}/${n}.py"
    if [[ ! -e ${f} ]]; then
        cp template.py "${f}"
    fi
done
for i in in.txt ex.txt; do
    f="${dir}/${i}"
    if [[ ! -e ${f} ]]; then
        touch "${f}"
    fi
done
