FROM ocaml/opam:debian-ocaml-4.12

ENV DEBIAN_FRONTEND=noninteractive


# RUN sudo apt update && apt install -y \
#     curl \
#     git \
#     build-essential 

RUN sudo apt-get update

RUN sudo apt-get install -y libgmp-dev
RUN sudo apt-get install -y pkg-config    

RUN sudo apt-get install -y time



WORKDIR /propsynth

# Copy application files into the container
COPY . .

RUN sudo chown -R opam:opam /propsynth

ENV PATH /usr/local/bin:$PATH

RUN sudo apt-get install -y opam

RUN opam init --disable-sandboxing --auto-setup && \
    eval $(opam env) && \
    opam install -y "z3>=4.7.1" menhir ocamlbuild ocamlfind


#RUN sudo opam init --disable-sandboxing --auto-setup
RUN which ocaml
RUN ocaml -version

# RUN sudo opam install -y  "z3>=4.7.1"

# RUN sudo opam install -y menhir
# RUN sudo opam install -y ocamlbuild
# RUN sudo opam install -y ocamlfind
# RUN eval $(opam env)

RUN eval $(opam env) && echo $PATH && which ocamlbuild
RUN sudo apt-get install -y python3 



# # Install Haskell Stack
# #RUN sudo apt-get update && sudo apt-get install -y haskell-stack

# RUN sudo apt-get update && sudo apt-get install -y \
#   haskell-stack \
#   libz3-dev z3 \
#   libtinfo-dev libgmp-dev zlib1g-dev

# # Build Synquid
# WORKDIR /propsynth/synquid


# RUN stack setup && stack build


# # Set back to root work directory
# WORKDIR /propsynth


CMD ["bash"] 
